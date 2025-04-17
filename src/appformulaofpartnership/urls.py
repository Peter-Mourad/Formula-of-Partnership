from fastapi import APIRouter

from appformulaofpartnership.views import register, dashboard

api_router = APIRouter()
api_router.include_router(register.router, tags=["register"])
api_router.include_router(dashboard.router, tags=["dashboard"])
