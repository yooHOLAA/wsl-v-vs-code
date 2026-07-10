from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db.db import Base
from sqlalchemy.orm import relationship

# Таблица категорий книг
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    
    # У одной категории может быть много книг
    books = relationship('Book', back_populates='category')

# Таблица книг
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    url = Column(String, nullable=True)
    
    # Связывает книгу с категорией
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    # Книга принадлежит одной категории
    category = relationship('Category', back_populates='books')