from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel


class BaseRepo:
    def __init__(self, session: AsyncSession, model):
        self.session = session
        self.model = model

    async def create(self, obj: BaseModel):
        db_obj = self.model(**obj.dict())
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def find(self, obj_id: int):
        db_obj = await self.session.execute(
            select(self.model).where(self.model.id == int(obj_id))
        )
        return db_obj.scalar_one_or_none()

    async def delete(self, db_obj):
        await self.session.delete(db_obj)
        await self.session.commit()

    async def update(self, db_obj, updates: BaseModel):
        for i, j in updates.dict(exclude_unset=True).items():
            setattr(db_obj, i, j)

        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

