from sqlalchemy.ext.asyncio import AsyncSession
from .repo import UserRepo
from .schemas import UserSchema, UpdateUser
from fastapi.exceptions import HTTPException
from .security.utils import create_password_hash


class UserService:
    def __init__(self, session: AsyncSession):
        self.user_repo = UserRepo(session)

    async def create_user(self, user: UserSchema):
        user.password = create_password_hash(user.password)
        new_user = await self.user_repo.create(user)
        if new_user is not None:
            return new_user
        else:
            return HTTPException(400, detail='Something went wrong')

    async def search_user_by_id(self, user_id: int):
        if user_id is None:
            return HTTPException(422, detail='Unprocessable Entity')

        user = await self.user_repo.find(user_id)
        if user is None:
            return HTTPException(404, detail=f'Not Found user with id-{user_id}')
        return user

    async def update_user_by_id(self, updates: UpdateUser):
        if updates.id is None:
            return HTTPException(422, detail='Unprocessable Entity')

        user = await self.user_repo.find(updates.id)
        if user is None:
            return HTTPException(404, detail=f'Not Found user with id-{updates.id}')

        if updates.password is not None:
            updates.password = create_password_hash(updates.password)
        updated_user = await self.user_repo.update(user, updates)
        if updated_user is None:
            return HTTPException(400, detail='Something went wrong')

        return updated_user

    async def delete_user_by_id(self, user_id: int):
        if user_id is None:
            return HTTPException(422, detail='Unprocessable Entity')

        user = await self.user_repo.find(user_id)
        if user is None:
            return HTTPException(404, detail=f'Not Found user with id-{user_id}')

        await self.user_repo.delete(user)

        return {"message": "User deleted", "user": user}


