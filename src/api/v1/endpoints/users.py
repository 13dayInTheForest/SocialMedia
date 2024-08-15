from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.database import get_session
from src.schemas.users import *
from src.crud import create_users_service


router = APIRouter()


@router.post('/create')
async def create_user(user: UserSchema, session: AsyncSession = Depends(get_session)):
    service = await create_users_service(session)
    return await service.create(user)


@router.get('/get')
async def get_user(user_id, session: AsyncSession = Depends(get_session)):
    service = await create_users_service(session)
    return await service.search_by_id(user_id)


@router.patch('/update')
async def get_user(updates: UpdateUser, session: AsyncSession = Depends(get_session)):
    service = await create_users_service(session)
    return await service.update_by_id(updates)


@router.delete('/delete')
async def get_user(user_id, session: AsyncSession = Depends(get_session)):
    service = await create_users_service(session)
    return await service.delete_by_id(user_id)
