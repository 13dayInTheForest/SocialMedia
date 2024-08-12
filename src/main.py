from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager
from database.database import *
from api.v1 import v1_api_router


app = FastAPI()
app.include_router(v1_api_router, prefix='/api/v1')


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