from fastapi import FastAPI
from app.routes.recommendation import router

app = FastAPI()

app.include_router(router)