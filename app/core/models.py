from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    submitted_by = Column(Integer, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationships
    students = relationship("Student", back_populates="submitted_user")
    courses = relationship("Course", back_populates="submitted_user")
    departments = relationship("Department", back_populates="submitted_user")
    attendance = relationship("AttendanceLog", back_populates="submitted_user")


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String, nullable=False)
    submitted_by = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    submitted_user = relationship("User", back_populates="departments")
    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    class_name = Column(String, nullable=True)
    submitted_by = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    department = relationship("Department", back_populates="students")
    submitted_user = relationship("User", back_populates="students")
    attendance = relationship("AttendanceLog", back_populates="student")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    semester = Column(String, nullable=True)
    class_name = Column(String, nullable=True)
    lecture_hours = Column(Integer, nullable=True)
    submitted_by = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    department = relationship("Department", back_populates="courses")
    submitted_user = relationship("User", back_populates="courses")
    attendance = relationship("AttendanceLog", back_populates="course")


class AttendanceLog(Base):
    __tablename__ = "attendance_log"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    present = Column(Boolean, default=False)
    submitted_by = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student = relationship("Student", back_populates="attendance")
    course = relationship("Course", back_populates="attendance")
    submitted_user = relationship("User", back_populates="attendance")
