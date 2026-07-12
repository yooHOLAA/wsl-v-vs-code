from pydantic import BaseModel, ConfigDict
from typing import Optional

# ==========================================
# Схемы для категорий (Category)
# ==========================================

# Базовая схема: какие поля нужны при создании/обновлении категории
class CategoryBase(BaseModel):
    title: str

# Схема для создания категории (наследуем от базовой)
class CategoryCreate(CategoryBase):
    pass

# Схема для обновления категории (title опционален, можно менять не всё)
class CategoryUpdate(BaseModel):
    title: Optional[str] = None

# Схема ответа: что возвращаем клиенту (добавляем id)
class CategoryResponse(CategoryBase):
    id: int

    # Говорим Pydantic, что можно работать с объектами SQLAlchemy
    model_config = ConfigDict(from_attributes=True)


# ==========================================
# Схемы для книг (Book)
# ==========================================

# Базовая схема: какие поля нужны при создании/обновлении книги
class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: Optional[str] = None
    category_id: int

# Схема для создания книги
class BookCreate(BookBase):
    pass

# Схема для обновления книги (все поля опциональны)
class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

# Схема ответа: что возвращаем клиенту (добавляем id)
class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)