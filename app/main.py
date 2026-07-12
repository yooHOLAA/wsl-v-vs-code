from fastapi import FastAPI
from .api import books, categories

# Создаем объект FastAPI
app = FastAPI(
    title="Bookstore API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

# Подключаем роутеры (эндпоинты)
app.include_router(categories.router)
app.include_router(books.router)

# Эндпоинт для проверки, что сервис жив
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API работает!"}

# Корневой эндпоинт
@app.get("/")
def root():
    return {"message": "Добро пожаловать в Bookstore API! Перейди в /docs для документации."}