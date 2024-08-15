from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from typing import TypeVar, Generic
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel


SchemaType = TypeVar('SchemaType', bound=BaseModel)


class BaseService:
    def __init__(self, session: AsyncSession, repository, model):
        self.repo = repository(session, model)

    async def create(self, obj_schema: SchemaType):
        db_obj = await self.repo.create(obj_schema)
        if db_obj is not None:
            return db_obj
        else:
            raise HTTPException(400, detail='Something went wrong')

    async def search_by_id(self, obj_id):
        if not obj_id.isdigit():
            raise HTTPException(422, detail='Unprocessable Entity')

        db_obj = await self.repo.find(obj_id)
        if db_obj is None:
            raise HTTPException(404, detail=f'Not Found id-{obj_id}')
        return db_obj

    async def update_by_id(self, updates: SchemaType):
        if updates.id != int:
            raise HTTPException(422, detail='Unprocessable Entity')

        db_obj = await self.repo.find(updates.id)
        if db_obj is None:
            raise HTTPException(404, detail=f'Not Found id-{updates.id}')

        updated_obj = await self.repo.update(db_obj, updates)
        if updated_obj is None:
            raise HTTPException(400, detail=f'Something went wrong, {updates}')

        return updated_obj

    async def delete_by_id(self, obj_id):
        if not obj_id.isdigit():
            raise HTTPException(422, detail='Unprocessable Entity')

        db_obj = await self.repo.find(obj_id)
        if db_obj is None:
            raise HTTPException(404, detail=f'Not Found id-{obj_id}')

        await self.repo.delete(db_obj)

        return {"message": "User deleted", "user": db_obj}


