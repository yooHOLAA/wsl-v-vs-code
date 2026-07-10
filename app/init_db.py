# Импортируем инструменты для подключения и создания таблиц
from db.db import engine, Base, SessionLocal
# Импортируем наши CRUD функции
from db.crud import create_category, create_book

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)
print("Таблицы созданы!")

# Получаем сессию для работы с БД
db = SessionLocal()

try:
    # Добавляем две категории
    cat1 = create_category(db, title="Фантастика")
    cat2 = create_category(db, title="Классика")
    print(f"Добавлены категории: {cat1.title}, {cat2.title}")

    # К каждой категории добавляем по 2 книги
    create_book(db, title="Дюна", description="Эпическая сага о пустынной планете", price=500.0, url="", category_id=cat1.id)
    create_book(db, title="Марсианин", description="Выживание на Марсе", price=450.0, url="", category_id=cat1.id)
    
    create_book(db, title="1984", description="Знаменитая антиутопия", price=300.0, url="", category_id=cat2.id)
    create_book(db, title="Война и мир", description="Роман Льва Толстого", price=800.0, url="", category_id=cat2.id)
    
    print("База данных успешно заполнена книгами!")
    
finally:
    db.close()