from typing import Any, List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, models
from app.api import deps
from app.schemas.food_item import FoodItem, FoodItemCreate, FoodItemUpdate

router = APIRouter()


@router.get("/", response_model=List[FoodItem])
def read_food_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve food items for the current user.
    """
    if category:
        food_items = crud.food_item.get_by_category(
            db, category=category, owner_id=current_user.id, skip=skip, limit=limit
        )
    else:
        food_items = crud.food_item.get_multi_by_owner(
            db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return food_items


@router.post("/", response_model=FoodItem)
def create_food_item(
    *,
    db: Session = Depends(deps.get_db),
    food_item_in: FoodItemCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new food item for the current user.
    """
    food_item = crud.food_item.create_with_owner(
        db=db, obj_in=food_item_in, owner_id=current_user.id
    )
    return food_item


@router.get("/expiring-soon/", response_model=List[FoodItem])
def read_expiring_food_items(
    db: Session = Depends(deps.get_db),
    days: int = Query(7, description="Number of days to check for expiration"),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve food items that are expiring soon for the current user.
    """
    food_items = crud.food_item.get_expiring_soon(
        db, days=days, owner_id=current_user.id, skip=skip, limit=limit
    )
    return food_items


@router.get("/{food_item_id}", response_model=FoodItem)
def read_food_item(
    *,
    db: Session = Depends(deps.get_db),
    food_item_id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get food item by ID.
    """
    food_item = crud.food_item.get(db=db, id=food_item_id)
    if not food_item:
        raise HTTPException(status_code=404, detail="Food item not found")
    if food_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return food_item


@router.put("/{food_item_id}", response_model=FoodItem)
def update_food_item(
    *,
    db: Session = Depends(deps.get_db),
    food_item_id: UUID,
    food_item_in: FoodItemUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a food item.
    """
    food_item = crud.food_item.get(db=db, id=food_item_id)
    if not food_item:
        raise HTTPException(status_code=404, detail="Food item not found")
    if food_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    food_item = crud.food_item.update(db=db, db_obj=food_item, obj_in=food_item_in)
    return food_item


@router.delete("/{food_item_id}", response_model=FoodItem)
def delete_food_item(
    *,
    db: Session = Depends(deps.get_db),
    food_item_id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a food item.
    """
    food_item = crud.food_item.get(db=db, id=food_item_id)
    if not food_item:
        raise HTTPException(status_code=404, detail="Food item not found")
    if food_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    food_item = crud.food_item.remove(db=db, id=food_item_id)
    return food_item