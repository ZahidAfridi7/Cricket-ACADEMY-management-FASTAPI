from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.crud.player import create_new_player,get_all_players,get_player_by_id,delete_player,update_player
from app.schemas.player import PlayerCreate,PlayerResponse,PlayerUpdate
from app.db.models.player import Player

router = APIRouter()

@router.post("/register", response_model=PlayerResponse)
async def add_player(player:PlayerCreate,db:AsyncSession):
    new_player = create_new_player(db,player)
    return new_player


@router.get('/all_players',response_model=PlayerResponse)
async def all_player(db:AsyncSession):
    return await get_all_players(db)

@router.get("/{player_id}",response_model=PlayerResponse)
async def get_player(player_id:int, db:AsyncSession):
    player = get_player_by_id(db,player_id)
    if player is None:
        raise HTTPException(status_code=404,detail="player not found")
    return player

@router.put("/update/{player_id}",response_model=PlayerResponse)
async def update(player_id:int,player_update:PlayerUpdate,db:AsyncSession):
    updated_data = update_player(db,player_id,player_update)
    if not updated_data:
        raise HTTPException(status_code=404,detail="player not found")
    
    return updated_data


@router.delete("delete/{player_id}",response_model=PlayerResponse)
async def delete(player_id:int,db:AsyncSession):
    player_delete = delete_player(db,player_id)
    if not player_delete:
        raise HTTPException(status_code=404, detail="player not found")
    return player_delete
