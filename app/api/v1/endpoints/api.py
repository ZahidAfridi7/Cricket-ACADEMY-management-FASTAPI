from fastapi import FastAPI,APIRouter

router = APIRouter()

from app.api.v1.endpoints import(
    player,
)
