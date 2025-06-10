from typing import List, Optional, Dict, Any, Union
from uuid import UUID

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.food_item import FoodItem
from app.models.user import User
from app.schemas.food_item import FoodItemCreate, FoodItemUpdate


class CRUDFoodItem(CRUDBase[FoodItem, FoodItemCreate, FoodItemUpdate]):
    def get_by_barcode(self, db: Session, *, barcode: str, owner_id: UUID) -> Optional[FoodItem]:
        return db.query(FoodItem).filter(FoodItem.barcode == barcode, FoodItem.owner_id == owner_id).first()

    def get_by_category(self, db: Session, *, category: str, owner_id: UUID, skip: int = 0, limit: int = 100) -> List[FoodItem]:
        return db.query(FoodItem).filter(FoodItem.category == category, FoodItem.owner_id == owner_id).offset(skip).limit(limit).all()

    def get_expiring_soon(self, db: Session, *, days: int = 7, owner_id: UUID, skip: int = 0, limit: int = 100) -> List[FoodItem]:
        from datetime import datetime, timedelta
        expiry_date = datetime.now().date() + timedelta(days=days)
        return (
            db.query(FoodItem)
            .filter(FoodItem.expiration_date <= expiry_date)
            .filter(FoodItem.expiration_date >= datetime.now().date())
            .filter(FoodItem.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_multi_by_owner(
        self, db: Session, *, owner_id: UUID, skip: int = 0, limit: int = 100
    ) -> List[FoodItem]:
        return (
            db.query(self.model)
            .filter(FoodItem.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def create_with_owner(
        self, db: Session, *, obj_in: FoodItemCreate, owner_id: UUID
    ) -> FoodItem:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


food_item = CRUDFoodItem(FoodItem)