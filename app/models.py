from datetime import datetime
from typing import Optional, List
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


# Report Models
class UserStatistics(BaseModel):
    """Statistics for a user's items"""
    total_items: int = Field(..., description="Total number of items")
    total_value: float = Field(..., description="Total value of all items")
    average_item_price: float = Field(..., description="Average price of items")
    items: List[ItemResponse] = Field(..., description="List of user's items")


class UserSummaryItem(BaseModel):
    """User summary item in users summary report"""
    user: UserResponse = Field(..., description="User information")
    statistics: UserStatistics = Field(..., description="User statistics")


class UsersSummaryResponse(BaseModel):
    """Response model for users summary report"""
    total_users: int = Field(..., description="Total number of users")
    users_summary: List[UserSummaryItem] = Field(..., description="List of users with their statistics")


class ItemWithOwner(BaseModel):
    """Item with owner information"""
    item: ItemResponse = Field(..., description="Item information")
    owner: Optional[UserResponse] = Field(None, description="Owner information")


class ItemsStatistics(BaseModel):
    """Overall items statistics"""
    total_items: int = Field(..., description="Total number of items")
    total_value: float = Field(..., description="Total value of all items")
    average_price: float = Field(..., description="Average item price")
    min_price: float = Field(..., description="Minimum item price")
    max_price: float = Field(..., description="Maximum item price")


class ItemsSummaryResponse(BaseModel):
    """Response model for items summary report"""
    statistics: ItemsStatistics = Field(..., description="Overall statistics")
    items: List[ItemWithOwner] = Field(..., description="List of items with owners")


class UserReportStatistics(BaseModel):
    """Statistics for a user report"""
    total_items: int = Field(..., description="Total number of items")
    total_value: float = Field(..., description="Total value of all items")
    average_item_price: float = Field(..., description="Average item price")
    min_item_price: float = Field(..., description="Minimum item price")
    max_item_price: float = Field(..., description="Maximum item price")


class UserReportResponse(BaseModel):
    """Response model for user detailed report"""
    user: UserResponse = Field(..., description="User information")
    items: List[ItemResponse] = Field(..., description="List of user's items")
    statistics: UserReportStatistics = Field(..., description="User statistics")


class UserStats(BaseModel):
    """User statistics for system overview"""
    user_id: int = Field(..., description="User ID")
    user_name: str = Field(..., description="User full name")
    user_email: str = Field(..., description="User email")
    item_count: int = Field(..., description="Number of items")
    total_value: float = Field(..., description="Total value of items")


class SystemOverviewStats(BaseModel):
    """System overview statistics"""
    total_users: int = Field(..., description="Total number of users")
    total_items: int = Field(..., description="Total number of items")
    total_value: float = Field(..., description="Total value of all items")
    average_item_price: float = Field(..., description="Average item price")


class SystemOverviewResponse(BaseModel):
    """Response model for system overview report"""
    overview: SystemOverviewStats = Field(..., description="System overview statistics")
    top_users_by_item_count: List[UserStats] = Field(..., description="Top 5 users by item count")
    top_users_by_total_value: List[UserStats] = Field(..., description="Top 5 users by total value")
    all_user_statistics: List[UserStats] = Field(..., description="Statistics for all users")


class PriceRangeFilters(BaseModel):
    """Price range filters"""
    min_price: Optional[float] = Field(None, description="Minimum price filter")
    max_price: Optional[float] = Field(None, description="Maximum price filter")


class ItemsByPriceRangeResponse(BaseModel):
    """Response model for items by price range report"""
    filters: PriceRangeFilters = Field(..., description="Applied filters")
    total_items: int = Field(..., description="Total number of items matching filters")
    items: List[ItemWithOwner] = Field(..., description="List of items with owners")

