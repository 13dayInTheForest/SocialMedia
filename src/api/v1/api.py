from fastapi import APIRouter
from .endpoints import users
from .endpoints import posts


v1_api_router = APIRouter(
    prefix='/api/v1'
)

v1_api_router.include_router(users.router, prefix='/users')
v1_api_router.include_router(posts.router, prefix='/posts')

