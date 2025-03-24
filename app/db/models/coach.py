from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from app.db.base_class import Base


class Coach(Base):
    __tablename__ = "coaches"
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)
    experence = Column(String, nullable=False)
    role = Column(String, nullable=False)
    email = Column(String,nullable=True)
    phone = Column(String, nullable=False)  
    address = Column(String,nullable=False)