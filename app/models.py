from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# User Models
class UserBase(BaseModel):
    """Base user model with common fields"""
    email: EmailStr = Field(..., description="User email address")
    full_name: str = Field(..., min_length=1, max_length=100, description="User full name")


class UserCreate(UserBase):
    """Model for creating a new user"""
    pass


class UserUpdate(BaseModel):
    """Model for updating user information"""
    email: Optional[EmailStr] = Field(None, description="User email address")
    full_name: Optional[str] = Field(None, min_length=1, max_length=100, description="User full name")


class UserResponse(UserBase):
    """Model for user response"""
    id: int = Field(..., description="User unique identifier")
    created_at: datetime = Field(..., description="User creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="User last update timestamp")

    class Config:
        from_attributes = True


# Item Models
class ItemBase(BaseModel):
    """Base item model with common fields"""
    title: str = Field(..., min_length=1, max_length=200, description="Item title")
    description: Optional[str] = Field(None, max_length=1000, description="Item description")
    price: float = Field(..., gt=0, description="Item price (must be greater than 0)")


class ItemCreate(ItemBase):
    """Model for creating a new item"""
    pass


class ItemUpdate(BaseModel):
    """Model for updating item information"""
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Item title")
    description: Optional[str] = Field(None, max_length=1000, description="Item description")
    price: Optional[float] = Field(None, gt=0, description="Item price (must be greater than 0)")


class ItemResponse(ItemBase):
    """Model for item response"""
    id: int = Field(..., description="Item unique identifier")
    owner_id: int = Field(..., description="ID of the user who owns this item")
    created_at: datetime = Field(..., description="Item creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Item last update timestamp")

    class Config:
        from_attributes = True


# Error Models
class ErrorResponse(BaseModel):
    """Standard error response model"""
    detail: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code for programmatic handling")

