from fastapi import APIRouter
from app.src.routers import health_check

router = APIRouter()
router.include_router(health_check.router)
