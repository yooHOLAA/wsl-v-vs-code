# WSL
#print("Hello, world!")

# PostgreSQL
from db.db import SessionLocal
from db.crud import get_categories, get_books

# Получаем сессию для работы с базой
db = SessionLocal()

try:
    print("=== СПИСОК КАТЕГОРИЙ ===")
    # Получаем все категории и выводим их
    categories = get_categories(db)
    for cat in categories:
        print(f"ID: {cat.id} | Название: {cat.title}")

    print("\n=== СПИСОК КНИГ ===")
    # Получаем все книги и выводим их
    books = get_books(db)
    for book in books:
        print(f"ID: {book.id} | Название: {book.title} | Цена: {book.price} руб. | Категория ID: {book.category_id}")
        
finally:
    # Закрываем сессию в конце
    db.close()