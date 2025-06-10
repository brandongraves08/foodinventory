from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.food_item import FoodItem
from app.schemas.food_item import FoodItemCreate, FoodItemUpdate


class CRUDFoodItem(CRUDBase[FoodItem, FoodItemCreate, FoodItemUpdate]):
    def get_by_barcode(self, db: Session, *, barcode: str) -> Optional[FoodItem]:
        return db.query(FoodItem).filter(FoodItem.barcode == barcode).first()

    def get_by_category(self, db: Session, *, category: str, skip: int = 0, limit: int = 100) -> List[FoodItem]:
        return db.query(FoodItem).filter(FoodItem.category == category).offset(skip).limit(limit).all()

    def get_expiring_soon(self, db: Session, *, days: int = 7, skip: int = 0, limit: int = 100) -> List[FoodItem]:
        from datetime import datetime, timedelta
        expiry_date = datetime.now().date() + timedelta(days=days)
        return (
            db.query(FoodItem)
            .filter(FoodItem.expiration_date <= expiry_date)
            .filter(FoodItem.expiration_date >= datetime.now().date())
            .offset(skip)
            .limit(limit)
            .all()
        )


food_item = CRUDFoodItem(FoodItem)
