from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from src.database.database import get_session
from src.schemas.users import *
from src.crud import create_users_service
from src.dependencies.auth import get_current_user
from src.core.security import create_access_token


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
async def update_user(updates: UpdateUser, session: AsyncSession = Depends(get_session)):
    service = await create_users_service(session)
    return await service.update_by_id(updates)


@router.delete('/delete')
async def delete_user(user_id, session: AsyncSession = Depends(get_session)):
    service = await create_users_service(session)
    return await service.delete_by_id(user_id)


@router.post('/token/')
async def get_token(user: UserAuth):
    return create_access_token(user.dict())


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get('/self')
async def get_self(
        token: str = Depends(oauth2_scheme),
        session: AsyncSession = Depends(get_session)
):
    return get_current_user(session, token)
