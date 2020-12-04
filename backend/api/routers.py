from fastapi import APIRouter

from backend.api.endpoint import quizz

api_router = APIRouter()
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(quizz.router, tags=["blog"])