from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class CompanySchema(BaseModel):
    id: int | None
    name: str
    profile_id: int | None
    direction: str | None
    description: str | None
    inn: int
    ogrn: int
    logo: str | None


    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestCompany(BaseModel):
    parameter: CompanySchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class ContactsSchema(BaseModel):
    id: int | None
    id_com: int | None
    name: str
    surname: str
    phone: str
    email: str
    photo: str | None

    class Config:
        orm_mode = True

class RequestContacts(BaseModel):
    parameter: ContactsSchema = Field(...)


class JobsSchema(BaseModel):
    id: int | None
    name: str
    id_com: int | None

    class Config:
        orm_mode = True


class RequestJobs(BaseModel):
    parameter: JobsSchema = Field(...)


class TeamsSchema(BaseModel):
    id: int | None
    job_id: int | None
    student_id: str | None

    class Config:
        orm_mode = True
