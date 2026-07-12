from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

# Импортируем наши модули
from ..db import db, crud
from .. import schemas

# Создаем роутер с префиксом /books
router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

# Зависимость для получения сессии БД (такая же, как в categories.py)
def get_db_session():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

# 1. READ: Получить все книги (с фильтрацией по категории)
@router.get("/", response_model=List[schemas.BookResponse])
def read_books(category_id: Optional[int] = Query(None, description="ID категории для фильтрации"), db: Session = Depends(get_db_session)):
    return crud.get_books(db, category_id=category_id)

# 2. READ: Получить книгу по ID
@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db_session)):
    db_book = crud.get_book_by_id(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

# 3. CREATE: Создать новую книгу
@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db_session)):
    # Валидация бизнес-логики: проверяем, существует ли такая категория
    category = crud.get_category_by_id(db, category_id=book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    return crud.create_book(
        db=db, 
        title=book.title, 
        description=book.description, 
        price=book.price, 
        url=book.url, 
        category_id=book.category_id
    )

# 4. UPDATE: Обновить книгу
@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db_session)):
    # Если при обновлении меняем категорию, проверяем её существование
    if book.category_id is not None:
        category = crud.get_category_by_id(db, category_id=book.category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Категория не найдена")
            
    db_book = crud.update_book(
        db=db, 
        book_id=book_id, 
        title=book.title, 
        description=book.description, 
        price=book.price, 
        url=book.url
    )
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

# 5. DELETE: Удалить книгу
@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db_session)):
    success = crud.delete_book(db=db, book_id=book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")