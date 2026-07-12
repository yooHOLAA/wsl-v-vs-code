from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Импортируем наши модули
from ..db import db, crud
from .. import schemas

# Создаем роутер с префиксом /categories
router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

# Зависимость для получения сессии БД
def get_db_session():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

# 1. READ: Получить все категории
@router.get("/", response_model=List[schemas.CategoryResponse])
def read_categories(db: Session = Depends(get_db_session)):
    return crud.get_categories(db)

# 2. READ: Получить категорию по ID
@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db_session)):
    db_category = crud.get_category_by_id(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category

# 3. CREATE: Создать новую категорию
@router.post("/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db_session)):
    return crud.create_category(db=db, title=category.title)

# 4. UPDATE: Обновить категорию
@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db_session)):
    db_category = crud.update_category(db=db, category_id=category_id, new_title=category.title)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category

# 5. DELETE: Удалить категорию
@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db_session)):
    success = crud.delete_category(db=db, category_id=category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Категория не найдена")