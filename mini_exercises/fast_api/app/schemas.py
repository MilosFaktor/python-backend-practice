from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


class PostDeleted(BaseModel):
    deleted: int
