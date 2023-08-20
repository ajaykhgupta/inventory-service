from fastapi import APIRouter
from inventory.controller import inventory_controller

v1_api_router = APIRouter()
v1_api_router.include_router(inventory_controller.router, prefix="/api/v1")
