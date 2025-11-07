from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String)
    confidence = Column(String)
    create_at = Column(DateTime, default=func.utcnow)
