from fastapi import APIRouter

from app.api.api_v1.endpoints import food_items, barcode, image_analysis

api_router = APIRouter()
api_router.include_router(food_items.router, prefix="/food-items", tags=["food-items"])
api_router.include_router(barcode.router, prefix="/barcode", tags=["barcode"])
api_router.include_router(image_analysis.router, prefix="/image-analysis", tags=["image-analysis"])
