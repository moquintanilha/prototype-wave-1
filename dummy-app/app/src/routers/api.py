from fastapi import APIRouter
from app.src.routers import health_check, create_people

router = APIRouter()
router.include_router(health_check.router)
router.include_router(create_people.router)
