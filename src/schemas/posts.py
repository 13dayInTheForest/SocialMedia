from pydantic import BaseModel
from datetime import datetime


class PostsSchema(BaseModel):
    title: str
    text: str
    file_url: str


class PostsFilter(BaseModel):
    id: int = None
    title: str = None
    text: str = None
    file_url: str = None
    user_id: int = None
    published_at: datetime = None
    updated: bool = None
    updated_at: datetime = None

