from sqlalchemy.orm import Session
from models import Company, Contact, Jobs


def get_company(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()


def get_company_by_id(db: Session, book_id: int):
    return db.query(Company).filter(Company.id == company_id).first()


def create_company(db: Session, book: CompanySchema):
    _book = Company(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def remove_company(db: Session, book_id: int):
    _book = get_company_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()


def update_company(db: Session, book_id: int, title: str, description: str):
    _book = get_company_by_id(db=db, book_id=book_id)

    _book.title = title
    _book.description = description

    db.commit()
    db.refresh(_book)
    return _book