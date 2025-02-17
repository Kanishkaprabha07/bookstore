from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str = Field(..., min_length=13, max_length=13, pattern="^\d{13}$")
    price: float

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = Field(None, min_length=13, max_length=13, pattern="^\d{13}$")
    price: Optional[float] = None

class BookResponse(BookBase):
    id: UUID

    class Config:
        from_attributes = True
