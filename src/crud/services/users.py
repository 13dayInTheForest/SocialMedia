from fastapi.exceptions import HTTPException
from src.core.security import create_password_hash
from .base import BaseService
from src.core.security import verify_password


class UserService(BaseService):
    async def create(self, obj_schema):
        obj_schema.password = create_password_hash(obj_schema.password)
        db_obj = await self.repo.create(obj_schema)
        if db_obj is not None:
            return db_obj
        else:
            raise HTTPException(400, detail='Something went wrong')

    async def update_by_id(self, updates):
        if type(updates.id) != int:
            raise HTTPException(422, detail='Unprocessable Entity')

        db_obj = await self.repo.find(updates.id)
        if db_obj is None:
            raise HTTPException(404, detail=f'Not Found id-{updates.id}')

        updates.password = create_password_hash(updates.password)
        updated_obj = await self.repo.update(db_obj, updates)

        if updated_obj is None:
            raise HTTPException(400, detail=f'Something went wrong, {updates}')
        return updated_obj

    async def verify_user(self, user_id: int, password: str):
        if password is None:
            raise HTTPException(400, detail='')
        user = await self.repo.find(user_id)

        if user is None:
            raise HTTPException(400, detail='user is not exist')

        if not verify_password(password, user.password):
            raise HTTPException(400, detail='incorrect login or password')
        return True




