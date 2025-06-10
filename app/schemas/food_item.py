from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
import uuid


class FoodItemBase(BaseModel):
    name: str
    barcode: Optional[str] = None
    category: Optional[str] = None
    quantity: int = 1
    expiration_date: Optional[date] = None
    image_url: Optional[str] = None
    source: str = "manual"  # barcode|vision|manual


class FoodItemCreate(FoodItemBase):
    pass


class FoodItemUpdate(BaseModel):
    name: Optional[str] = None
    barcode: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    expiration_date: Optional[date] = None
    image_url: Optional[str] = None


class FoodItem(FoodItemBase):
    id: uuid.UUID
    added_at: datetime

    class Config:
        from_attributes = True
