from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints.api import router
from app.db.session import database

app = FastAPI(title=settings.PROJECT_NAME)

# Include all endpoints under /api/v1
app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def root():
    return {"message": "Welcome to Afridi Cricket Academy Management System"}
