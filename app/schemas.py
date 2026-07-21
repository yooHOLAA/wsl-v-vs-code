from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

# ==========================================
# Схемы для категорий (Category)
# ==========================================

class CategoryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Название категории")

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ==========================================
# Схемы для книг (Book)
# ==========================================

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Название книги")
    description: str = Field(..., min_length=1, description="Описание книги")
    price: float = Field(..., gt=0, description="Цена книги должна быть больше 0")
    url: Optional[str] = Field(None, description="Ссылка на книгу")
    category_id: int = Field(..., description="ID категории")

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)