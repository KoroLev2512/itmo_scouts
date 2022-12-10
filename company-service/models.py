from sqlalchemy import DateTime, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    profile_id = Column(Integer)
    direction = Column(Integer)
    description = Column(String)
    inn = Column(Integer)
    ogrn = Column(Integer)
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
    name = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    company = relationship("Company")


class Teams(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("job.id"))
    student_id = Column(String)
