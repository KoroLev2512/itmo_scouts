from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv
from models import Company, Contact, Jobs, Teams
from schemas import CompanySchema, ContactsSchema, JobsSchema, TeamsSchema

import router

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["COMPANY_DATABASE_URL"])


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/companies")
def get_company(skip: int = 0, limit: int = 100):
    return db.session.query(Company).offset(skip).limit(limit).all()


@app.get("/companies/{company_id}")
def get_company_by_id(company_id: int):
    return db.session.query(Company).filter(Company.id == company_id).first()


@app.post("/companies", response_model=CompanySchema)
def create_company(company: CompanySchema):
    _company = Company(
        name=company.name,
        profile_id=company.profile_id,
        direction=company.direction,
        description=company.description,
        inn=company.inn,
        ogrn=company.ogrn,
        logo=company.logo
)
    db.session.add(_company)
    db.session.commit()
    return _company


def remove_company(company_id: int):
    _company = get_company_by_id(company_id)
    db.session.delete(_company)
    db.session.commit()


@app.put("/companies")
def update_company(company_id: int, name: str, description: str):
    _company = get_company_by_id(company_id)

    _company.name = name
    _company.description = description

    db.session.commit()
    db.session.refresh(_company)
    return _company


def get_contact(skip: int = 0, limit: int = 100):
    return db.session.query(Contact).offset(skip).limit(limit).all()


def get_contact_by_id(contact_id: int):
    return db.session.query(Contact).filter(Contact.id == contact_id).first()


def create_contact(contact: ContactsSchema):
    _contact = Contact(id_com=contact.id_com,
                       name=contact.name,
                       surname=contact.surname,
                       phone=contact.phone,
                       email=contact.email,
                       photo=contact.photo
                       )
    db.session.add(_contact)
    db.session.commit()
    db.session.refresh(_contact)
    return _contact


def remove_contact(contact_id: int):
    _contact = get_contact_by_id(contact_id)
    db.session.delete(_contact)
    db.session.commit()


def update_contact(contact_id: int, name: str, description: str):
    _contact = get_contact_by_id(contact_id)

    _contact.session.name = name
    _contact.session.description = description

    db.session.commit()
    db.session.refresh(_contact)
    return _contact


@app.get("/jobs")
def get_jobs(skip: int = 0, limit: int = 100):
    return db.session.query(Jobs).offset(skip).limit(limit).all()


@app.get("/jobs/{job_id}")
def get_jobs_by_id(jobs_id: int):
    return db.session.query(Jobs).filter(Jobs.id == jobs_id).first()


@app.post("/jobs", response_model=JobsSchema)
def create_jobs(jobs: JobsSchema):
    _jobs = Jobs(name=jobs.name, id_com=jobs.id_com)
    db.session.add(_jobs)
    db.session.commit()
    return _jobs


def remove_jobs(jobs_id: int):
    _jobs = get_jobs_by_id(jobs_id)
    db.session.delete(_jobs)
    db.session.commit()


def update_jobs(jobs_id: int, title: str, description: str):
    _jobs = get_jobs_by_id(jobs_id)

    _jobs.title = title
    _jobs.description = description

    db.session.commit()
    db.session.refresh(_jobs)
    return _jobs


@app.get("/teams")
def get_teams(skip: int = 0, limit: int = 100):
    return db.session.query(Teams).offset(skip).limit(limit).all()


@app.get("/teams/{teams_id}")
def get_teams_by_id(teams_id: int):
    return db.session.query(Teams).filter(Teams.id == teams_id).first()


@app.post("/teams", response_model=TeamsSchema)
def create_teams(teams: TeamsSchema):
    _teams = Teams(
        job_id=teams.job_id,
        student_id=teams.student_id)
    db.session.add(_teams)
    db.session.commit()
    return _teams


def remove_teams(teams_id: int):
    _teams = get_teams_by_id(teams_id)
    db.session.delete(_teams)
    db.session.commit()


def update_teams(teams_id: int, name: str, description: str):
    _teams = get_teams_by_id(teams_id)

    _teams.name = name
    _teams.description = description

    db.session.commit()
    db.session.refresh(_teams)
    return _teams

#@app.post("/add-company/", response_model=CompanySchema)
#def add_company(company: CompanySchema):
#    db_company = ModelCompany(title=company.name)

#app.include_router(router, prefix="/company", tags=["company"])
