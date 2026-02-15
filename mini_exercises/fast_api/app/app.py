import os
import shutil
import tempfile
import uuid
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.ddb import Post, User, create_db_and_tables, get_async_session
from app.images import URL_ENDPOINT, imagekit
from app.logging_setup import setup_logging
from app.schemas import PostCreate, UserCreate, UserRead, UserUpdate
from app.users import auth_backend, current_active_user, fastapi_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


logger = setup_logging()

app = FastAPI(lifespan=lifespan)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/")
def root():
    logger.info("Root endpoint hit")
    return {"message": "root"}


@app.post("/upload")
async def upload(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    logger.info(f"Upload endpoint hit for file: {file.filename}")

    temp_file_path = None
    filename = file.filename or "upload.bin"
    suffix = os.path.splitext(filename)[1]

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_file_path = temp_file.name
            file.file.seek(0)
            shutil.copyfileobj(file.file, temp_file)

        with open(temp_file_path, "rb") as f:
            file_bytes = f.read()

        upload_response = imagekit.files.upload(
            file=file_bytes,
            file_name=filename,
            use_unique_file_name=True,
            tags=["backend-upload"],
        )

        url = getattr(upload_response, "url", None)
        name = getattr(upload_response, "name", None)
        if not url or not name:
            raise HTTPException(status_code=502, detail="ImageKit upload failed")

        post = Post(
            user_id=user.id,
            caption=caption,
            url=url,
            file_type="video"
            if (file.content_type or "").startswith("video/")
            else "image",
            file_name=name,
        )
        session.add(post)
        await session.commit()
        await session.refresh(post)
        return post

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        await file.close()


@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    result = await session.execute(select(User))
    users = {row[0].id: row[0] for row in result.all()}
    user_dict = {str(u.id): u.email for u in users.values()}

    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id": str(post.id),
                "user_id": str(post.user_id),
                "caption": post.caption,
                "url": post.url,
                "file_type": post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat(),
                "is_owner": post.user_id == user.id,
                "email": user_dict.get(str(post.user_id), "Unknown"),
            }
        )
    return {"posts": posts_data}


@app.delete("/post/{post_id}")
async def delete_post(
    post_id: str,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    try:
        post_uuid = uuid.UUID(post_id)

        result = await session.execute(select(Post).where(Post.id == post_uuid))
        post = result.scalars().first()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        if post.user_id is not user.id:
            raise HTTPException(
                status_code=403, detail="Not authorized to delete this post"
            )

        await session.delete(post)
        await session.commit()

        return {"success": True, "message": "Post deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
