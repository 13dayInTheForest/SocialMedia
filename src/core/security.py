from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from src.core.config import settings
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.KEY_PRIVATE, settings.ALGORITHM)
    return encoded_jwt


def decode_token(token: str):
    decoded_jwt = jwt.decode(token, settings.KEY_PRIVATE, settings.ALGORITHM)
    return decoded_jwt


def create_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, pass_hash: str):
    return pwd_context.verify(password, pass_hash)
