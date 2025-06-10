from sqlalchemy import Column, String, Integer, Date, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.base_class import Base


class FoodItem(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, index=True)
    barcode = Column(String, index=True)
    category = Column(String, index=True)
    quantity = Column(Integer, default=1)
    expiration_date = Column(Date, nullable=True)
    image_url = Column(String, nullable=True)
    source = Column(String, nullable=False)  # barcode|vision|manual
    added_at = Column(DateTime, default=func.now())
    
    # User relationship
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    owner = relationship("User", back_populates="food_items")