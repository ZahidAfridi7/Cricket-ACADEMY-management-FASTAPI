from pydantic import BaseModel, EmailStr
from typing import Optional

class CoachCreate(BaseModel):
    id: int
    name:str
    age:int
    grade:str
    experence:str
    role:str
    email:EmailStr
    phone:str
    address:str
    
    
class CoachUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None
    experence: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class CoachResponse(BaseModel):
    id: int
    name: str
    age: int
    grade: Optional[str] = None
    experence: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr]=None
    phone: str
    address: str

    class Config:
        orm_mode = True

                                       