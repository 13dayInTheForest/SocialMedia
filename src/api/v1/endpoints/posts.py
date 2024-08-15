from fastapi import APIRouter, Depends
from src.schemas.posts import CreatePosts
from src.crud import create_posts_service
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.database import get_session


router = APIRouter()


@router.post('/create')
async def create_post(post: CreatePosts, session: AsyncSession = Depends(get_session)):
    service = await create_posts_service(session)
    return await service.create(post)


@router.get('/get')
async def create_post(post: CreatePosts, start: int, limit: int, session: AsyncSession = Depends(get_session)):
    service = await create_posts_service(session)
    return await service.create(post)


@router.patch('/update')
async def create_post(post: CreatePosts, session: AsyncSession = Depends(get_session)):
    service = await create_posts_service(session)
    return await service.create(post)


@router.delete('/delete')
async def create_post(post: CreatePosts, session: AsyncSession = Depends(get_session)):
    service = await create_posts_service(session)
    return await service.create(post)



