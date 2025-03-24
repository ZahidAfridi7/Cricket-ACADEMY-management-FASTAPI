from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.player import Player
from app.schemas.player import PlayerCreate,PlayerResponse,PlayerUpdate


async def create_new_player(db:AsyncSession,player:PlayerCreate):
    new_player = Player(
        id = player.id,
        name = player.name,
        age = player.age,
        role = player.role,
        batting_style = player.batting_style,
        bowling_style = player.bowling_style,
        phone = player.phone,
        address = player.address
    ) 
    db.add(new_player)
    await db.commit()
    await db.refresh(new_player)
    return new_player

async def get_all_players(db:AsyncSession,skip:int=0):
    result = db.execute(select(Player).offset(skip))
    return result.scalars().all()

async def get_player_by_id(db:AsyncSession,player_id:int):
    result = db.execute(select(Player).where(Player.id==player_id))
    return result.scalar()

async def update_player(db:AsyncSession,player_id:int,player_update:PlayerUpdate):
    player = get_player_by_id(db,player_id)
    
    if not player:
            return None
        
    update_data = player_update.dict(exclude_unset=True)
        
    for key,value in update_data.items():
            setattr(player,key,value)
            
    await db.commit()
    await db.refresh(player)
    return player



async def delete_player(db:AsyncSession,player_id:int):
    result = db.execute(select(Player).where(Player.id == player_id))
    player = result.scalar()
    
    if not player:
        return None
    await db.delete(player)
    await db.commit()
    return player        