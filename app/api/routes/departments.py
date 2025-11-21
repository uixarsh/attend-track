from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.models import Department
from app.schemas import (
    DepartmentCreate, DepartmentUpdate, DepartmentResponse
)

router = APIRouter(
    prefix="/api/v1/department",
    tags=["Departments"]
)


# ----------------------------------------
# DEPARTMENTS
# ----------------------------------------
@router.post("/", response_model=DepartmentResponse)
def create_department(request: DepartmentCreate, db: Session = Depends(get_db)):
    dept = Department(**request.dict())
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept


@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(department_id: int, db: Session = Depends(get_db)):
    dept = db.query(Department).filter(Department.id == department_id).first()
    if not dept:
        raise HTTPException(404, "Department not found")
    return dept


@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department(department_id: int, request: DepartmentUpdate, db: Session = Depends(get_db)):
    dept = db.query(Department).filter(Department.id == department_id).first()
    if not dept:
        raise HTTPException(404, "Department not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(dept, key, value)

    db.commit()
    db.refresh(dept)
    return dept