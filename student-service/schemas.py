from pydantic import BaseModel
from typing import Optional


class Citizenship(BaseModel):
    id: int | None
    name: str

    class Config:
        orm_mode = True


class Student(BaseModel):
    id: int | None
    isu: int
    profile_id: int | None
    thumbnail: str | None
    name: str
    surname: str
    patronymic: str | None
    phone: str
    citizenship_id: int | None
    vk_link: str | None
    email: str
    description: str | None

    class Config:
        orm_mode = True


class Project(BaseModel):
    id: int | None
    name: str
    student_id: int | None
    description: str | None

    class Config:
        orm_mode = True


class Resume(BaseModel):
    id: int | None
    student_id: int
    description: str

    class Config:
        orm_mode = True


class Application(BaseModel):
    id: int | None
    student_id: int
    job_id: int

    class Config:
        orm_mode = True
