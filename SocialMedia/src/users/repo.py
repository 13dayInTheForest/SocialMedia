from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import *
from src.database.models import Users


class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: UserSchema):
        new_user = Users(
            name=user.name,
            password=user.password,
            bio=user.bio,
            superuser=user.superuser
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user

    async def find(self, user_id: int):
        user = await self.session.execute(
            select(Users).where(Users.id == int(user_id))
        )
        return user.scalar_one_or_none()

    async def delete(self, user_id: int):
        await self.session.delete(user_id)
        await self.session.commit()

    async def update(self, user: Users, updates: UpdateUser):
        if updates.name is not None:
            user.name = updates.name
        if updates.password is not None:
            user.password = updates.password
        if updates.bio is not None:
            user.bio = updates.bio
        if updates.superuser is not None:
            user.superuser = updates.superuser
        await self.session.commit()
        await self.session.refresh(user)
        return user

