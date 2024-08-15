from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class CreatePosts(BaseModel):
    title:str
    text: str
    file_url: str
    user_id: int
    category_id: int
    anonymously: bool


class PostsFilter(BaseModel):
    id: int = None
    title: str = None
    text: str = None
    file_url: str = None
    user_id: int = None
    published_at: datetime = None
    updated: bool = None
    updated_at: datetime = None


class GetPosts(BaseModel):
    start: int = 0
    limit: int = 5
    filter: PostsFilter



