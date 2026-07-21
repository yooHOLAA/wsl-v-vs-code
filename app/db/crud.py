from sqlalchemy.orm import Session
from .models import Category, Book

# ==========================================
# CRUD для таблицы Categories (Категории)
# ==========================================

# Create: Создание категории
def create_category(db: Session, title: str):
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Read: Получение всех категорий
def get_categories(db: Session):
    return db.query(Category).all()

# Update: Обновление категории
def update_category(db: Session, category_id: int, new_title: str):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db_category.title = new_title
        db.commit()
        db.refresh(db_category)
    return db_category

# Delete: Удаление категории
def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False


# ==========================================
# CRUD для таблицы Books (Книги)
# ==========================================

# Create: Создание книги
def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Read: Получение всех книг
def get_books(db: Session):
    return db.query(Book).all()

# Update: Обновление книги
def update_book(db: Session, book_id: int, title: str = None, description: str = None, price: float = None, url: str = None):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        if title: db_book.title = title
        if description: db_book.description = description
        if price: db_book.price = price
        if url: db_book.url = url
        db.commit()
        db.refresh(db_book)
    return db_book

# Delete: Удаление книги
def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False

# Получить категорию по ID (нужно для API)
def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

# Получить все книги (с опциональной фильтрацией по категории)
def get_books(db: Session, category_id: int = None):
    query = db.query(Book)
    if category_id is not None:
        query = query.filter(Book.category_id == category_id)
    return query.all()

# Получить книгу по ID (нужно для API)
def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# Проверка существования категории по названию
def get_category_by_title(db: Session, title: str):
    return db.query(Category).filter(Category.title == title).first()

# Проверка существования книги по названию в конкретной категории
def get_book_by_title(db: Session, title: str, category_id: int):
    return db.query(Book).filter(Book.title == title, Book.category_id == category_id).first()