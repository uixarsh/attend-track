from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

# -----------------------------
# Users
# -----------------------------
class UserBase(BaseModel):
    type: str
    full_name: str
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    type: Optional[str] = None


class UserResponse(UserBase):
    id: int
    submitted_by: Optional[int] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# -----------------------------
# Department
# -----------------------------
class DepartmentBase(BaseModel):
    department_name: str


class DepartmentCreate(DepartmentBase):
    submitted_by: Optional[int] = None


class DepartmentUpdate(BaseModel):
    department_name: Optional[str] = None


class DepartmentResponse(DepartmentBase):
    id: int
    submitted_by: Optional[int] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# -----------------------------
# Student
# -----------------------------
class StudentBase(BaseModel):
    full_name: str
    department_id: int
    class_name: Optional[str]


class StudentCreate(StudentBase):
    submitted_by: Optional[int] = None


class StudentUpdate(BaseModel):
    full_name: Optional[str]
    department_id: Optional[int]
    class_name: Optional[str]


class StudentResponse(StudentBase):
    id: int
    submitted_by: Optional[int] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# -----------------------------
# Course
# -----------------------------
class CourseBase(BaseModel):
    course_name: str
    department_id: int
    semester: Optional[str]
    class_name: Optional[str]
    lecture_hours: Optional[int]


class CourseCreate(CourseBase):
    submitted_by: Optional[int] = None


class CourseUpdate(BaseModel):
    course_name: Optional[str]
    department_id: Optional[int]
    semester: Optional[str]
    class_name: Optional[str]
    lecture_hours: Optional[int]


class CourseResponse(CourseBase):
    id: int
    submitted_by: Optional[int] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# -----------------------------
# Attendance
# -----------------------------
class AttendanceBase(BaseModel):
    student_id: int
    course_id: int
    present: bool


class AttendanceCreate(AttendanceBase):
    submitted_by: Optional[int] = None


class AttendanceUpdate(BaseModel):
    present: Optional[bool] = None


class AttendanceResponse(AttendanceBase):
    id: int
    submitted_by: Optional[int] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True