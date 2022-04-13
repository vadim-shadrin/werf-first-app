from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from os import getenv


PYTHONUNBUFFERED=1
SOURCE_BASE_URL = getenv('SOURCE_BASE_URL')
API_VERSION = getenv('API_VERSION')

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware,
    secret_key = getenv('SECRET_KEY'),
)

@app.get(f"{API_VERSION}/healthcheck")
def helthcheck_():
    return {"health": "ok"}
