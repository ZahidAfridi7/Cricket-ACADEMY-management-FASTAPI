from pydantic import BaseModel
from typing import List,Optional

class PlayerCreate(BaseModel):
    id:int
    name:str
    age:int
    role:str
    batting_style:str
    bowling_style:str
    phone:int
    address:str
      
    class config:
       from_attributes = True  
       
class PlayerResponse(BaseModel):
    id:int
    name:str
    role:str
    address:str
    
    class config:
        orm_mode = True


class PlayerUpdate:
    name:Optional[str]=None
    age:Optional[int]=None
    role:Optional[str]=None
    phone:Optional[int]=None
    address:Optional[int]=None           