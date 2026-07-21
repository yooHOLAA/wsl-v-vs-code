from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from ..db import crud
from ..db.db import get_db
from .. import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[schemas.BookResponse])
def read_books(category_id: Optional[int] = Query(None, description="ID категории для фильтрации"), db: Session = Depends(get_db)):
    return crud.get_books(db, category_id=category_id)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # 1. Проверяем, существует ли категория
    category = crud.get_category_by_id(db, category_id=book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    # 2. Проверяем, нет ли уже такой книги в этой категории
    existing_book = crud.get_book_by_title(db, title=book.title, category_id=book.category_id)
    if existing_book:
        raise HTTPException(
            status_code=400, 
            detail=f"Книга с названием '{book.title}' уже существует в этой категории"
        )

    # 3. Если всё ок, создаем
    return crud.create_book(
        db=db, 
        title=book.title, 
        description=book.description, 
        price=book.price, 
        url=book.url, 
        category_id=book.category_id
    )

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    if book.category_id is not None:
        category = crud.get_category_by_id(db, category_id=book.category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Категория не найдена")
    db_book = crud.update_book(db=db, book_id=book_id, title=book.title, description=book.description, price=book.price, url=book.url)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db=db, book_id=book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")