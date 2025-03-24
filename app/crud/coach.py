from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.coach import Coach
from app.schemas.coach import CoachCreate,CoachResponse,CoachUpdate


async def create_coach(db:AsyncSession,coach:CoachCreate):
    new_coach = Coach(
        id = coach.id,
        name = coach.name,
        age = coach.age,
        grade = coach.grade,
        experence = coach.experence,
        role = coach.role,
        phone = coach.phone,
        address = coach.address
)
    db.add(new_coach)
    await db.commit()
    await db.refresh(new_coach)
    return new_coach


async def get_all_coaches(db:AsyncSession,coach_id:int=0):
    result = await db.execute(select(Coach).offset(coach_id))
    return result.scalars().all()


async def get_coach_by_id(db:AsyncSession,coach_id:int):
    result = await db.execute(select(Coach).where(Coach.id==coach_id))
    return result.scalar()


async def update_coaches(db:AsyncSession,coach_id:int,coach_update:CoachUpdate):
    coach = await get_coach_by_id(db,coach_id)
    if not coach:
        return None
    
    update_data = coach_update.dict(exclude_unset=True)
    for key,value in update_data.items():
        setattr(coach,key,value)
        
    await db.commit()
    await db.refresh(coach)
    return coach    
        
async def delete_coach(db:AsyncSession,coach_id:int):
    result = await db.execute(select(Coach).where(Coach.id==coach_id))
    if not result:
        return None
    await db.delete(result)
    await db.commit()
    return result        