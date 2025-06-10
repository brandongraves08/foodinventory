from typing import Any
import base64
from io import BytesIO

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
import openai
from PIL import Image

from app.core.config import settings
from app.schemas.food_item import FoodItemCreate
from app.api import deps
from app import models

router = APIRouter()


@router.post("/", response_model=FoodItemCreate)
async def analyze_image(
    file: UploadFile = File(...),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Analyze food item image using OpenAI Vision API.
    """
    try:
        # Check if OpenAI API key is set
        if not settings.OPENAI_API_KEY:
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
            
        # Set OpenAI API key
        openai.api_key = settings.OPENAI_API_KEY
        
        # Read and validate image
        contents = await file.read()
        try:
            image = Image.open(BytesIO(contents))
            # Convert to RGB if needed
            if image.mode != "RGB":
                image = image.convert("RGB")
            
            # Save to buffer for base64 encoding
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image: {str(e)}")
            
        # Prepare prompt for OpenAI
        prompt = """
        Analyze this food item image and extract the following information in JSON format:
        1. name: The name of the food item
        2. category: The category (e.g., Dairy, Produce, Meat, etc.)
        3. estimated_expiration_days: Estimated days until expiration (integer)
        
        Only respond with valid JSON. Do not include any explanations or notes.
        """
        
        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        # Parse response
        import json
        try:
            result = json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            # If not valid JSON, try to extract JSON from the response
            content = response.choices[0].message.content
            # Find JSON-like content between curly braces
            start = content.find('{')
            end = content.rfind('}')
            if start != -1 and end != -1:
                try:
                    result = json.loads(content[start:end+1])
                except json.JSONDecodeError:
                    raise HTTPException(status_code=500, detail="Failed to parse AI response")
            else:
                raise HTTPException(status_code=500, detail="Failed to parse AI response")
        
        # Calculate expiration date if provided
        expiration_date = None
        if "estimated_expiration_days" in result and result["estimated_expiration_days"]:
            from datetime import datetime, timedelta
            days = int(result["estimated_expiration_days"])
            expiration_date = (datetime.now() + timedelta(days=days)).date()
        
        # Create food item
        food_item = FoodItemCreate(
            name=result.get("name", "Unknown Food Item"),
            category=result.get("category", "Unknown"),
            expiration_date=expiration_date,
            source="vision"
        )
        
        return food_item
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing image: {str(e)}")