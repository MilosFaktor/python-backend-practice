import os
import shutil
import tempfile
import uuid
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.ddb import Post, create_db_and_tables, get_async_session
from app.images import URL_ENDPOINT, imagekit
from app.logging_setup import setup_logging
from app.schemas import PostCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


logger = setup_logging()

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    logger.info("Root endpoint hit")
    return {"message": "root"}


@app.post("/upload")
async def upload(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session),
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
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id": str(post.id),
                "caption": post.caption,
                "url": post.url,
                "file_type": post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat(),
            }
        )
    return {"posts": posts_data}
