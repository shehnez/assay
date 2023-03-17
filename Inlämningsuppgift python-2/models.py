from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    aurthor = Column(String(255))
    description = Column(String(300))
    rating = Column(Integer)