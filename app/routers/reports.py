"""
Reports router - Generates reports using internal APIs
"""
from typing import List, Optional
from fastapi import APIRouter, HTTPException, status
from app.models import (
    UsersSummaryResponse,
    UserSummaryItem,
    UserStatistics,
    ItemsSummaryResponse,
    ItemsStatistics,
    ItemWithOwner,
    UserReportResponse,
    UserReportStatistics,
    SystemOverviewResponse,
    SystemOverviewStats,
    UserStats,
    ItemsByPriceRangeResponse,
    PriceRangeFilters
)
from app.routers import users, items

router = APIRouter()


@router.get(
    "/users-summary",
    response_model=UsersSummaryResponse,
    summary="Users summary report",
    description="Generates a summary report of all users with their item statistics"
)
async def get_users_summary() -> UsersSummaryResponse:
    """
    Get users summary report.
    
    Returns a report with all users and statistics about their items:
    - Total number of items per user
    - Total value of items per user
    - Average item price per user
    """
    users_list = await users.get_users()
    
    items_list = await items.get_items()
    
    summary = []
    for user in users_list:
        user_items = [item for item in items_list if item.owner_id == user.id]
        
        total_items = len(user_items)
        total_value = sum(item.price for item in user_items)
        avg_price = total_value / total_items if total_items > 0 else 0.0
        
        summary.append(
            UserSummaryItem(
                user=user,
                statistics=UserStatistics(
                    total_items=total_items,
                    total_value=round(total_value, 2),
                    average_item_price=round(avg_price, 2),
                    items=user_items
                )
            )
        )
    
    return UsersSummaryResponse(
        total_users=len(users_list),
        users_summary=summary
    )


@router.get(
    "/items-summary",
    response_model=ItemsSummaryResponse,
    summary="Items summary report",
    description="Generates a summary report of all items with owner information"
)
async def get_items_summary() -> ItemsSummaryResponse:
    """
    Get items summary report.
    
    Returns a report with all items and their owner information:
    - Item details
    - Owner information
    - Overall statistics
    """
    items_list = await items.get_items()
    

    users_list = await users.get_users()
    
    users_dict = {user.id: user for user in users_list}
    
    items_with_owners = []
    for item in items_list:
        owner = users_dict.get(item.owner_id)
        items_with_owners.append(
            ItemWithOwner(
                item=item,
                owner=owner if owner else None
            )
        )
    
    total_items = len(items_list)
    total_value = sum(item.price for item in items_list)
    avg_price = total_value / total_items if total_items > 0 else 0.0
    min_price = min(item.price for item in items_list) if items_list else 0.0
    max_price = max(item.price for item in items_list) if items_list else 0.0
    
    return ItemsSummaryResponse(
        statistics=ItemsStatistics(
            total_items=total_items,
            total_value=round(total_value, 2),
            average_price=round(avg_price, 2),
            min_price=round(min_price, 2),
            max_price=round(max_price, 2)
        ),
        items=items_with_owners
    )


@router.get(
    "/user/{user_id}",
    response_model=UserReportResponse,
    summary="User detailed report",
    description="Generates a detailed report for a specific user with all their items"
)
async def get_user_report(user_id: int) -> UserReportResponse:
    """
    Get detailed report for a specific user.
    
    - **user_id**: The ID of the user to generate the report for
    
    Returns detailed information about the user and all their items.
    """
    try:
        user = await users.get_user(user_id)
    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    user_items = await items.get_items_by_user(user_id)
    
    total_items = len(user_items)
    total_value = sum(item.price for item in user_items)
    avg_price = total_value / total_items if total_items > 0 else 0.0
    min_price = min(item.price for item in user_items) if user_items else 0.0
    max_price = max(item.price for item in user_items) if user_items else 0.0
    
    return UserReportResponse(
        user=user,
        items=user_items,
        statistics=UserReportStatistics(
            total_items=total_items,
            total_value=round(total_value, 2),
            average_item_price=round(avg_price, 2),
            min_item_price=round(min_price, 2),
            max_item_price=round(max_price, 2)
        )
    )


@router.get(
    "/system-overview",
    response_model=SystemOverviewResponse,
    summary="System overview report",
    description="Generates a comprehensive overview report of the entire system"
)
async def get_system_overview() -> SystemOverviewResponse:
    """
    Get system overview report.
    
    Returns a comprehensive report with:
    - Total users
    - Total items
    - Overall statistics
    - Top users by item count
    - Top users by total value
    """
    users_list = await users.get_users()
    items_list = await items.get_items()
    
    total_users = len(users_list)
    total_items = len(items_list)
    total_value = sum(item.price for item in items_list)
    avg_price = total_value / total_items if total_items > 0 else 0.0
    
    user_stats = []
    for user in users_list:
        user_items = [item for item in items_list if item.owner_id == user.id]
        user_stats.append(
            UserStats(
                user_id=user.id,
                user_name=user.full_name,
                user_email=user.email,
                item_count=len(user_items),
                total_value=round(sum(item.price for item in user_items), 2)
            )
        )
    
    top_by_count = sorted(user_stats, key=lambda x: x.item_count, reverse=True)[:5]
    top_by_value = sorted(user_stats, key=lambda x: x.total_value, reverse=True)[:5]
    
    return SystemOverviewResponse(
        overview=SystemOverviewStats(
            total_users=total_users,
            total_items=total_items,
            total_value=round(total_value, 2),
            average_item_price=round(avg_price, 2)
        ),
        top_users_by_item_count=top_by_count,
        top_users_by_total_value=top_by_value,
        all_user_statistics=user_stats
    )


@router.get(
    "/items-by-price-range",
    response_model=ItemsByPriceRangeResponse,
    summary="Items by price range report",
    description="Generates a report of items filtered by price range"
)
async def get_items_by_price_range(
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
) -> ItemsByPriceRangeResponse:
    """
    Get items filtered by price range.
    
    - **min_price**: Minimum price filter (optional)
    - **max_price**: Maximum price filter (optional)
    
    Returns items within the specified price range with owner information.
    """
    items_list = await items.get_items()
    
    filtered_items = items_list
    if min_price is not None:
        filtered_items = [item for item in filtered_items if item.price >= min_price]
    if max_price is not None:
        filtered_items = [item for item in filtered_items if item.price <= max_price]
    
    users_list = await users.get_users()
    users_dict = {user.id: user for user in users_list}
    
    items_with_owners = []
    for item in filtered_items:
        owner = users_dict.get(item.owner_id)
        items_with_owners.append(
            ItemWithOwner(
                item=item,
                owner=owner if owner else None
            )
        )
    
    return ItemsByPriceRangeResponse(
        filters=PriceRangeFilters(
            min_price=min_price,
            max_price=max_price
        ),
        total_items=len(items_with_owners),
        items=items_with_owners
    )

