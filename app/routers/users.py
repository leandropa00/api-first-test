"""
Users router - Handles all user-related endpoints
"""
from typing import List
from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from app.models import UserCreate, UserUpdate, UserResponse

router = APIRouter()

users_db = {}
user_id_counter = 1


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Creates a new user with the provided information"
)
async def create_user(user: UserCreate) -> UserResponse:
    """
    Create a new user.
    
    - **email**: User's email address (must be valid email format)
    - **full_name**: User's full name (1-100 characters)
    """
    global user_id_counter
    
    for existing_user in users_db.values():
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    now = datetime.utcnow()
    new_user = {
        "id": user_id_counter,
        "email": user.email,
        "full_name": user.full_name,
        "created_at": now,
        "updated_at": None
    }
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    
    return UserResponse(**new_user)


@router.get(
    "",
    response_model=List[UserResponse],
    summary="Get all users",
    description="Retrieves a list of all users"
)
async def get_users() -> List[UserResponse]:
    """
    Get all users.
    
    Returns a list of all registered users.
    """
    return [UserResponse(**user) for user in users_db.values()]


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user by ID",
    description="Retrieves a specific user by their ID"
)
async def get_user(user_id: int) -> UserResponse:
    """
    Get user by ID.
    
    - **user_id**: The ID of the user to retrieve
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    return UserResponse(**users_db[user_id])


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update user",
    description="Updates an existing user's information"
)
async def update_user(user_id: int, user_update: UserUpdate) -> UserResponse:
    """
    Update user information.
    
    - **user_id**: The ID of the user to update
    - **email**: (Optional) New email address
    - **full_name**: (Optional) New full name
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    user = users_db[user_id]
    
    # Check if new email already exists (if provided)
    if user_update.email and user_update.email != user["email"]:
        for existing_user in users_db.values():
            if existing_user["email"] == user_update.email and existing_user["id"] != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )
    
    # Update user fields
    if user_update.email is not None:
        user["email"] = user_update.email
    if user_update.full_name is not None:
        user["full_name"] = user_update.full_name
    
    user["updated_at"] = datetime.utcnow()
    
    return UserResponse(**user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user",
    description="Deletes a user by their ID"
)
async def delete_user(user_id: int):
    """
    Delete user.
    
    - **user_id**: The ID of the user to delete
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    del users_db[user_id]
    return None
