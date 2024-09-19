from fastapi import APIRouter
from src.schemas.users import UserAuth


router = APIRouter()


@router.post('/token')
async def get_token(user: UserAuth):
    pass

