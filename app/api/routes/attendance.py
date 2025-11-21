from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.models import AttendanceLog
from app.schemas import (
    AttendanceCreate, AttendanceUpdate, AttendanceResponse
)

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)

# ----------------------------------------
# ATTENDANCE
# ----------------------------------------
@router.post("/", response_model=AttendanceResponse)
def create_attendance(request: AttendanceCreate, db: Session = Depends(get_db)):
    record = AttendanceLog(**request.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.get("/", response_model=list[AttendanceResponse])
def get_attendance(db: Session = Depends(get_db)):
    return db.query(AttendanceLog).all()


@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_record(attendance_id: int, db: Session = Depends(get_db)):
    record = db.query(AttendanceLog).filter(AttendanceLog.id == attendance_id).first()
    if not record:
        raise HTTPException(404, "Record not found")
    return record


@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(attendance_id: int, request: AttendanceUpdate, db: Session = Depends(get_db)):
    record = db.query(AttendanceLog).filter(AttendanceLog.id == attendance_id).first()
    if not record:
        raise HTTPException(404, "Record not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)
    return record