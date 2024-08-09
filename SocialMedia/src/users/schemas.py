from pydantic import BaseModel
from datetime import datetime


class UserSchema(BaseModel):
    name: str
    password: str
    bio: str
    superuser: bool


class UpdateUser(BaseModel):
    id: int
    name: str = None
    password: str = None
    bio: str = None
    superuser: bool = None



