from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from app.db.base_class import Base


class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    role = Column(String, nullable=False)
    batting_style = Column(String, nullable=True)
    bowling_style = Column(String, nullable=True)
    email = Column(String,nullable=True)
    phone = Column(String, nullable=False)  
    address = Column(String,nullable=False)
    