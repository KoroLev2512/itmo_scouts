from sqlalchemy.orm import Session
from models import Company, Contact, Jobs
from schemas import CompanySchema, ContactsSchema, JobsSchema


def get_company(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()


def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()


def create_company(db: Session, company: CompanySchema):
    _company = Company(name=company.name, description=company.description)
    db.add(_company)
    db.commit()
    db.refresh(_company)
    return _company


def remove_company(db: Session, company_id: int):
    _company = get_company_by_id(db=db, company_id=company_id)
    db.delete(_company)
    db.commit()


def update_company(db: Session, company_id: int, title: str, description: str):
    _company = get_company_by_id(db=db, company_id=company_id)

    _company.title = title
    _company.description = description

    db.commit()
    db.refresh(_company)
    return _company


def get_contact(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contact).offset(skip).limit(limit).all()


def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()


def create_contact(db: Session, contact: ContactsSchema):
    _contact = Contact(name=contact.name, description=contact.description)
    db.add(_contact)
    db.commit()
    db.refresh(_contact)
    return _contact


def remove_contact(db: Session, contact_id: int):
    _contact = get_contact_by_id(db=db, contact_id=contact_id)
    db.delete(_contact)
    db.commit()


def update_contact(db: Session, contact_id: int, title: str, description: str):
    _contact = get_contact_by_id(db=db, contact_id=contact_id)

    _contact.title = title
    _contact.description = description

    db.commit()
    db.refresh(_contact)
    return _contact


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Jobs).offset(skip).limit(limit).all()


def get_jobs_by_id(db: Session, jobs_id: int):
    return db.query(Jobs).filter(Jobs.id == jobs_id).first()


def create_jobs(db: Session, jobs: JobsSchema):
    _jobs = jobs(name=jobs.name, description=jobs.description)
    db.add(_jobs)
    db.commit()
    db.refresh(_jobs)
    return _jobs


def remove_jobs(db: Session, jobs_id: int):
    _jobs = get_jobs_by_id(db=db, jobs_id=jobs_id)
    db.delete(_jobs)
    db.commit()


def update_jobs(db: Session, jobs_id: int, title: str, description: str):
    _jobs = get_jobs_by_id(db=db, jobs_id=jobs_id)

    _jobs.title = title
    _jobs.description = description

    db.commit()
    db.refresh(_jobs)
    return _jobs
