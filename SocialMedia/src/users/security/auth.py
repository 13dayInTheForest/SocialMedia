from fastapi import APIRouter
from src.users.schemas import UserSchema


router = APIRouter()


@router.post('/token')
async def register_user(user: UserSchema):
    pass

