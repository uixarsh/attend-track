from fastapi import APIRouter

from app.api.routes import attendance, departments, students, users

api_router = APIRouter()
api_router.include_router(attendance.router)
api_router.include_router(students.router)
api_router.include_router(departments.router)
api_router.include_router(users.router)