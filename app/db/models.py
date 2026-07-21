from .db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    
    # ДОБАВЛЕНО: cascade="all, delete"
    books = relationship('Book', back_populates='category', cascade="all, delete")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    url = Column(String, nullable=True)
    
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship('Category', back_populates='books')