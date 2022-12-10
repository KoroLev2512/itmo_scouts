from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class CompanySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    profile_id: Optional[int] = None
    direction: Optional[str] = None
    description: Optional[str] = None
    inn: Optional[int] = None
    ogrn: Optional[int] = None
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

    id_com: Optional[int] = None