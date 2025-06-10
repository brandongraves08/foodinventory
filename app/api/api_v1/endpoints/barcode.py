from typing import Any

from fastapi import APIRouter, Depends, HTTPException
import requests

from app.core.config import settings
from app.schemas.food_item import FoodItemCreate
from app.api import deps
from app import models

router = APIRouter()


@router.get("/{barcode}", response_model=FoodItemCreate)
def lookup_barcode(
    barcode: str,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Lookup food item information using barcode from Open Food Facts API.
    """
    try:
        # Call Open Food Facts API
        response = requests.get(
            f"{settings.OPEN_FOOD_FACTS_API_URL}/product/{barcode}.json",
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        # Check if product was found
        if data.get("status") != 1 or not data.get("product"):
            raise HTTPException(status_code=404, detail="Product not found")
            
        product = data["product"]
        
        # Extract relevant information
        food_item = FoodItemCreate(
            name=product.get("product_name", "Unknown Product"),
            barcode=barcode,
            category=product.get("categories_tags", ["unknown"])[0].replace("en:", "") if product.get("categories_tags") else "unknown",
            image_url=product.get("image_url"),
            source="barcode"
        )
        
        return food_item
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Error contacting barcode API: {str(e)}")