from fastapi import FastAPI,APIRouter

router = APIRouter()

from app.api.v1.endpoints import(
    player,
)

router.include_router(player.router, prefix="/app/api/v1/player", tags=["Players"])