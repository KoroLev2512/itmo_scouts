from sqlalchemy import Column, Integer, String, ForeignKey, func
from config import Base
import DateTime


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    profile_id = (Integer)
    direction = Column(Integer)
    description = Column(String)
    inn = Column(Integer(10))
    ogrn = Column(Integer(13))
    logo = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, index=True)
    id_com = Column(Integer, ForeignKey("company.id"))
    name = Column(String)
    surname = Column(String)
    phone = Column(String)
    email = Column(String)
    photo = Column(String)


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    id_com = Column(Integer, ForeignKey("company.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())