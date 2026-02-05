# scratch.py
import asyncio

from sqlalchemy import select

from app.ddb import Post, get_async_session

"""
TESTING INTERACTING WITH DATABASE
"""


async def test():
    async for session in get_async_session():
        result = await session.execute(select(Post))
        posts = [row[0] for row in result.all()]

        posts_data = []
        for post in posts:
            print(
                {
                    "id": str(post.id),
                    "caption": post.caption,
                    "url": post.url,
                    "file_type": post.file_type,
                    "file_name": post.file_name,
                    "created_at": post.created_at.isoformat(),
                }
            )

        result1 = await session.execute(select(Post.id))
        ids = [str(i) for i in result1.scalars().all()]
        print(ids)


asyncio.run(test())
