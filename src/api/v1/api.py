from fastapi import APIRouter
from .endpoints import users


v1_api_router = APIRouter()

v1_api_router.include_router(users.router, prefix='/users')
