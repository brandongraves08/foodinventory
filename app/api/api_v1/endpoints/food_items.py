from typing import Any, List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db
from app.schemas.food_item import FoodItem, FoodItemCreate, FoodItemUpdate

router = APIRouter()


@router.get("/", response_model=List[FoodItem])
def read_food_items(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
) -> Any:
    """
    Retrieve food items.
    """
    if category:
        food_items = crud.food_item.get_by_category(db, category=category, skip=skip, limit=limit)
    else:
        food_items = crud.food_item.get_multi(db, skip=skip, limit=limit)
    return food_items


@router.post("/", response_model=FoodItem)
def create_food_item(
    *,
    db: Session = Depends(get_db),
    food_item_in: FoodItemCreate,
) -> Any:
    """
    Create new food item.
    """
    food_item = crud.food_item.create(db=db, obj_in=food_item_in)
    return food_item


@router.get("/expiring-soon/", response_model=List[FoodItem])
def read_expiring_food_items(
    db: Session = Depends(get_db),
    days: int = Query(7, description="Number of days to check for expiration"),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve food items that are expiring soon.
    """
    food_items = crud.food_item.get_expiring_soon(db, days=days, skip=skip, limit=limit)
    return food_items


@router.get("/{food_item_id}", response_model=FoodItem)
def read_food_item(
    *,
    db: Session = Depends(get_db),
    food_item_id: UUID,
) -> Any:
    """
    Get food item by ID.
    """
    food_item = crud.food_item.get(db=db, id=food_item_id)
    if not food_item:
        raise HTTPException(status_code=404, detail="Food item not found")
    return food_item


@router.put("/{food_item_id}", response_model=FoodItem)
def update_food_item(
    *,
    db: Session = Depends(get_db),
    food_item_id: UUID,
    food_item_in: FoodItemUpdate,
) -> Any:
    """
    Update a food item.
    """
    food_item = crud.food_item.get(db=db, id=food_item_id)
    if not food_item:
        raise HTTPException(status_code=404, detail="Food item not found")
    food_item = crud.food_item.update(db=db, db_obj=food_item, obj_in=food_item_in)
    return food_item


@router.delete("/{food_item_id}", response_model=FoodItem)
def delete_food_item(
    *,
    db: Session = Depends(get_db),
    food_item_id: UUID,
) -> Any:
    """
    Delete a food item.
    """
    food_item = crud.food_item.get(db=db, id=food_item_id)
    if not food_item:
        raise HTTPException(status_code=404, detail="Food item not found")
    food_item = crud.food_item.remove(db=db, id=food_item_id)
    return food_item
