from fastapi import APIRouter
from src.schemas.users import UserSchema


router = APIRouter()


@router.post('/token')
async def register_user(user: UserSchema):
    pass

