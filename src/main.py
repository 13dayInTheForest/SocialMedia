import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from contextlib import asynccontextmanager
from database.database import *
from api.v1 import v1_api_router


app = FastAPI()
app.include_router(v1_api_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield

app.router.lifespan_context = lifespan


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/')
async def index():
    return {'message': 'hello'}


if __name__ == '__main__':
    run('main:app', reload=True)