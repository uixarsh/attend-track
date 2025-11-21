from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import User, Department, Student, Course, AttendanceLog
from schemas import (
    UserCreate, UserResponse, UserUpdate,
    DepartmentCreate, DepartmentUpdate, DepartmentResponse,
    StudentCreate, StudentUpdate, StudentResponse,
    CourseCreate, CourseUpdate, CourseResponse,
    AttendanceCreate, AttendanceUpdate, AttendanceResponse
)

router = APIRouter(
    prefix="/api/v1",
    tags=["API v1"]
)


# ----------------------------------------
# USERS
# ----------------------------------------
@router.post("/users", response_model=UserResponse)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, request: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


# ----------------------------------------
# DEPARTMENTS
# ----------------------------------------
@router.post("/departments", response_model=DepartmentResponse)
def create_department(request: DepartmentCreate, db: Session = Depends(get_db)):
    dept = Department(**request.dict())
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept


@router.get("/departments", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()


@router.get("/departments/{department_id}", response_model=DepartmentResponse)
def get_department(department_id: int, db: Session = Depends(get_db)):
    dept = db.query(Department).filter(Department.id == department_id).first()
    if not dept:
        raise HTTPException(404, "Department not found")
    return dept


@router.put("/departments/{department_id}", response_model=DepartmentResponse)
def update_department(department_id: int, request: DepartmentUpdate, db: Session = Depends(get_db)):
    dept = db.query(Department).filter(Department.id == department_id).first()
    if not dept:
        raise HTTPException(404, "Department not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(dept, key, value)

    db.commit()
    db.refresh(dept)
    return dept


# ----------------------------------------
# STUDENTS
# ----------------------------------------
@router.post("/students", response_model=StudentResponse)
def create_student(request: StudentCreate, db: Session = Depends(get_db)):
    student = Student(**request.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


@router.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(404, "Student not found")
    return student


@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, request: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(404, "Student not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student


# ----------------------------------------
# COURSES
# ----------------------------------------
@router.post("/courses", response_model=CourseResponse)
def create_course(request: CourseCreate, db: Session = Depends(get_db)):
    course = Course(**request.dict())
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@router.get("/courses", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()


@router.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(404, "Course not found")
    return course


@router.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, request: CourseUpdate, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(404, "Course not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)
    return course


# ----------------------------------------
# ATTENDANCE
# ----------------------------------------
@router.post("/attendance", response_model=AttendanceResponse)
def create_attendance(request: AttendanceCreate, db: Session = Depends(get_db)):
    record = AttendanceLog(**request.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.get("/attendance", response_model=list[AttendanceResponse])
def get_attendance(db: Session = Depends(get_db)):
    return db.query(AttendanceLog).all()


@router.get("/attendance/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_record(attendance_id: int, db: Session = Depends(get_db)):
    record = db.query(AttendanceLog).filter(AttendanceLog.id == attendance_id).first()
    if not record:
        raise HTTPException(404, "Record not found")
    return record


@router.put("/attendance/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(attendance_id: int, request: AttendanceUpdate, db: Session = Depends(get_db)):
    record = db.query(AttendanceLog).filter(AttendanceLog.id == attendance_id).first()
    if not record:
        raise HTTPException(404, "Record not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)
    return record
