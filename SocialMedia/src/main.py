from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager
from database.database import *
from users import user_router


app = FastAPI()
app.include_router(user_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield



app.router.lifespan_context = lifespan


@app.get('/')
async def index():
    return {'message': 'hello'}


if __name__ == '__main__':
    run('main:app', reload=True)