from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class CompanySchema(BaseModel):
    id: int
    name: str
    profile_id: int
    direction: str
    description: Optional[str] = None
    inn: int
    ogrn: int
    logo: Optional[str] = None


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
    id: int
    name: str
    id_com: Optional[int] = None
    name: str
    surname: str
    phone: str
    email: str
    photo: Optional[str] = None

    class Config:
        orm_mode = True

class RequestContacts(BaseModel):
    parameter: ContactsSchema = Field(...)


class JobsSchema(BaseModel):
    id: int
    name: str
    id_com: Optional[int] = None

    class Config:
        orm_mode = True


class RequestJobs(BaseModel):
    parameter: JobsSchema = Field(...)


class TeamsSchema(BaseModel):
    id: int
    job_id: int
    student_id: list

    class Config:
        orm_mode = True
