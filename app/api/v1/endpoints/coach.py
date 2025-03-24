from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.coach import (
    create_coach,
    delete_coach,
    update_coaches,
    get_all_coaches,
    get_coach_by_id
)
from app.schemas.coach import CoachCreate,CoachResponse,CoachUpdate
from app.db.session import get_db


router = APIRouter()

@router.post("/coach_register",response_model=CoachResponse)
async def coach_create(coach:CoachCreate,db:AsyncSession=Depends(get_db)):
    new_coach = await create_coach(db,coach)
    
    return new_coach

@router.get("/all_coaches",response_model=list[CoachResponse])
async def get_coaches(db:AsyncSession=Depends(get_db)):
    return await get_all_coaches(db)


@router.get("/{coach_id}",response_model=CoachResponse)
async def get_coach(coach_id:int,db:AsyncSession=Depends(get_db)):
    coach = await get_coach_by_id(db,coach_id)
    if not coach:
        raise HTTPException(status_code=404, detail="no coach found")
    return coach

@router.put("/update_coach/{coach_id}",response_model=CoachResponse)
async def update_coach(coach_id:int,coach_update:CoachUpdate,db:AsyncSession=Depends(get_db)):
    updated_data = await update_coaches(db,coach_id,coach_update)
    if not updated_data:
        raise HTTPException(status_code=404,detail="no data found")
    return updated_data


@router.delete("/delete/{coach_id}", response_model=CoachResponse)
async def coach_delete(coach_id:int,db:AsyncSession=Depends(get_db)):
    delete = await delete_coach(db,coach_id)
    if not delete:
        raise HTTPException(status_code=404, detail="no coach found to delete")
    return delete


