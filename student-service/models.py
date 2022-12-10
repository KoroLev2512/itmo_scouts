from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    isu = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    profile_id = Column(Integer)
    thumbnail = Column(String)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    phone = Column(String)
    citizenship_id = Column(Integer, ForeignKey("citizenship.id"))
    vk_link = Column(String)
    email = Column(String)
    description = Column(String)

    user = relationship("User")
    citizenship = relationship("Citizenship")


class Citizenship(Base):
    __tablename__ = "citizenship"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey("student.id"))
    description = Column(String)

    student = relationship("Student")


class Resume(Base):
    __tablename__ = "resume"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    description = Column(String)

    student = relationship("Student")


class Applications(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    job_id = Column(Integer)

    student = relationship("Student")
