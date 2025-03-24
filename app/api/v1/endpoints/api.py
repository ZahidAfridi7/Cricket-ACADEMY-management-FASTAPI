from fastapi import FastAPI,APIRouter

router = APIRouter()

from app.api.v1.endpoints import(
    player,
    coach
)

router.include_router(player.router, prefix="/app/api/v1/player", tags=["Players"])
router.include_router(coach.router, prefix="/app/api/v1/coach", tags=["Coaches"])