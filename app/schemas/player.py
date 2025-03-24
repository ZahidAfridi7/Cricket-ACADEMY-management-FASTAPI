from pydantic import BaseModel, EmailStr
from typing import Optional


class PlayerCreate(BaseModel):
    id:int
    name: str
    age: int
    role: Optional[str] = None
    batting_style: Optional[str] = None
    bowling_style: Optional[str] = None
    email: EmailStr
    phone: str
    address: str


class PlayerUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None
    batting_style: Optional[str] = None
    bowling_style: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class PlayerResponse(BaseModel):
    id: int
    name: str
    age: int
    role: Optional[str] = None
    batting_style: Optional[str] = None
    bowling_style: Optional[str] = None
    email: Optional[EmailStr]=None
    phone: str
    address: str

    class Config:
        orm_mode = True
