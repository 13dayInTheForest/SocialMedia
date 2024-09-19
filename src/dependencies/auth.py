from sqlalchemy.ext.asyncio import AsyncSession
from src.core.security import decode_token
from jose import ExpiredSignatureError
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from src.database.models import Users


async def get_current_user(session: AsyncSession, token: str):
    try:
        token = decode_token(token)
        user = await session.execute(select(Users).where(Users.id == token['id']))
        return user.scalar_one_or_none()

    except ExpiredSignatureError:
        raise HTTPException(401, detail='Unauthorized')




