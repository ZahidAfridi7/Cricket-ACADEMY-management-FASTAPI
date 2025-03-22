from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.sql import func
from app.db.models.base import Base


class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    role = Column(String,nullable=False)
    batting_style = Column(String)
    bowling_style = Column(String)
    phone = Column(Integer,nullable=False)
    address = Column(String,nullable=False)
    
     