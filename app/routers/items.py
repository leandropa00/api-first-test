from typing import List
from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from app.models import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter()

items_db = {}
item_id_counter = 1


@router.post(
    "",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new item",
    description="Creates a new item with the provided information",
)
async def create_item(item: ItemCreate, owner_id: int) -> ItemResponse:
    """
    Create a new item.

    - **title**: Item title (1-200 characters)
    - **description**: Item description (optional, max 1000 characters)
    - **price**: Item price (must be greater than 0)
    - **owner_id**: ID of the user who owns this item
    """
    global item_id_counter

    now = datetime.utcnow()
    new_item = {
        "id": item_id_counter,
        "title": item.title,
        "description": item.description,
        "price": item.price,
        "owner_id": owner_id,
        "created_at": now,
        "updated_at": None,
    }
    items_db[item_id_counter] = new_item
    item_id_counter += 1

    return ItemResponse(**new_item)


@router.get(
    "",
    response_model=List[ItemResponse],
    summary="Get all items",
    description="Retrieves a list of all items",
)
async def get_items(skip: int = 0, limit: int = 100) -> List[ItemResponse]:
    """
    Get all items.

    - **skip**: Number of items to skip (for pagination)
    - **limit**: Maximum number of items to return (default: 100)

    Returns a list of all items with pagination support.
    """
    items_list = list(items_db.values())[skip : skip + limit]
    return [ItemResponse(**item) for item in items_list]


@router.get(
    "/user/{user_id}",
    response_model=List[ItemResponse],
    summary="Get items by user",
    description="Retrieves all items belonging to a specific user",
)
async def get_items_by_user(
    user_id: int,
    skip: int = 0,
    limit: int = 100
) -> List[ItemResponse]:
    """
    Get all items belonging to a specific user.

    - **user_id**: The ID of the user whose items to retrieve
    - **skip**: Number of items to skip (for pagination)
    - **limit**: Maximum number of items to return (default: 100)

    Returns a list of items owned by the specified user with pagination support.
    """
    # Filter items by owner_id
    user_items = [
        item for item in items_db.values()
        if item["owner_id"] == user_id
    ]
    
    # Apply pagination
    user_items = user_items[skip : skip + limit]
    
    return [ItemResponse(**item) for item in user_items]


@router.get(
    "/{item_id}",
    response_model=ItemResponse,
    summary="Get item by ID",
    description="Retrieves a specific item by its ID",
)
async def get_item(item_id: int) -> ItemResponse:
    """
    Get item by ID.

    - **item_id**: The ID of the item to retrieve
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )

    return ItemResponse(**items_db[item_id])


@router.put(
    "/{item_id}",
    response_model=ItemResponse,
    summary="Update item",
    description="Updates an existing item's information",
)
async def update_item(item_id: int, item_update: ItemUpdate) -> ItemResponse:
    """
    Update item information.

    - **item_id**: The ID of the item to update
    - **title**: (Optional) New title
    - **description**: (Optional) New description
    - **price**: (Optional) New price
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )

    item = items_db[item_id]

    if item_update.title is not None:
        item["title"] = item_update.title
    if item_update.description is not None:
        item["description"] = item_update.description
    if item_update.price is not None:
        item["price"] = item_update.price

    item["updated_at"] = datetime.utcnow()

    return ItemResponse(**item)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete item",
    description="Deletes an item by its ID",
)
async def delete_item(item_id: int):
    """
    Delete item.

    - **item_id**: The ID of the item to delete
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )

    del items_db[item_id]
    return None
