# Bookstore API

REST API для управления книгами и категориями. Написан на **FastAPI** + **SQLAlchemy** + **PostgreSQL**.

## Возможности

- CRUD операции для книг и категорий
- Фильтрация книг по категории
- Валидация данных через Pydantic
- Автоматическая Swagger-документация

## Технологии

- Python 3.14
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Pydantic

## Установка
1. Клонируем репозиторий:
   ```bash
   git clone https://github.com/yooHOLAA/wsl-v-vs-code.git
   cd wsl-v-vs-code

## Создаем и активируем виртуальное окружение
2. 
python3 -m venv venv
source venv/bin/activate

## Устонавливаем зависимости
3. 
pip install -r requirements.txt

## Настраиваем файл .env
4. 
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

## Создаем таблицы и заполняем тестовыми данными
5. 
python3 app/init_db.py

## Запуск сервера
uvicorn app.main:app --reload

http://127.0.0.1:8000/docs — интерактивная документация (Swagger)
http://127.0.0.1:8000/health — проверка работоспособности API