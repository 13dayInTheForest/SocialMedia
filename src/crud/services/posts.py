from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.repositories.posts import PostsRepo
from src.schemas.posts import *
from fastapi.exceptions import HTTPException
from src.core.security import create_password_hash
from src.database.models import Posts
from .base import BaseService


class PostService(BaseService):
    pass


