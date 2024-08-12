from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.services.users import UserService
from src.database.database import get_session
from src.schemas.users import *


router = APIRouter(
    prefix='/users'
)
router.include_router()

@router.post('/create')
async def create_user(user: UserSchema, session: AsyncSession = Depends(get_session)):
    service = UserService(session)
    return await service.create_user(user)


@router.get('/get')
async def get_user(user_id, session: AsyncSession = Depends(get_session)):
    service = UserService(session)
    return await service.search_user_by_id(user_id)


@router.patch('/update')
async def get_user(updates: UpdateUser, session: AsyncSession = Depends(get_session)):
    service = UserService(session)
    return await service.update_user_by_id(updates)


@router.delete('/delete')
async def get_user(user_id, session: AsyncSession = Depends(get_session)):
    service = UserService(session)
    return await service.delete_user_by_id(user_id)
