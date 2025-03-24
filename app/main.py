from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints.api import router

app = FastAPI(title=settings.PROJECT_NAME)

# Include all endpoints under /api/v1
app.include_router(router, prefix="/api/v1")

router.get("/")
async def root():
    return {"message": "Welcome to Afridi Cricket Academy Management System"}
