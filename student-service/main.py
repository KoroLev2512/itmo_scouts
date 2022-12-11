from fastapi import FastAPI, Body
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv
import os
import models
import schemas
from fastapi.responses import JSONResponse

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.Student):
    db_student = models.Student(
        isu=student.isu,
        profile_id=student.profile_id,
        thumbnail=student.thumbnail,
        name=student.name,
        surname=student.surname,
        patronymic=student.patronymic,
        phone=student.phone,
        citizenship_id=student.citizenship_id,
        vk_link=student.vk_link,
        email=student.email,
        description=student.description
    )
    db.session.add(db_student)
    db.session.commit()
    return db_student


@app.get("/students")
def get_students():
    students = db.session.query(models.Student).all()

    return students


@app.get("/students/{student_id}", response_model=schemas.Student)
def get_student(student_id: int):
    student = db.session.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        return JSONResponse(status_code=404, content={"message": "Student not found"})
    return student


@app.post("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int):
    student = get_student(student_id)
    db.session.delete(student)
    db.session.commit()
    return student


"""@app.put("/student/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, data=Body()):
    student = get_student(student_id)
    if data["isu"] is not None:
        student.isu = data["isu"]
    if data["profile_id"] is not None:
        student.profile_id = data["profile_id"]
    if data["thumbnail"] is not None:
        student.thumbnail = data["thumbnail"]
    if data["name"] is not None:
        student.name = data["name"]
    if data["surname"] is not None:
        student.surname = data["surname"]
    if data["patronymic"] is not None:
        student.patronymic = data["patronymic"]
    if data["phone"] is not None:
        student.phone = data["phone"]
    if data["citizenship_id"] is not None:
        student.citizenship_id = data["citizenship_id"]
    if data["vk_link"] is not None:
        student.vk_link = data["vk_link"]
    if data["email"] is not None:
        student.email = data["email"]
    if data["description"] is not None:
        student.description = data["description"]
    db.session.commit()
    return student"""


@app.post("/citizenship", response_model=schemas.Citizenship)
def create_citizenship(citizenship: schemas.Citizenship):
    db_citizenship = models.Citizenship(
        name=citizenship.name
    )
    db.session.add(db_citizenship)
    db.session.commit()
    return db_citizenship


@app.post("/resume", response_model=schemas.Resume)
def create_resume(resume: schemas.Resume):
    db_resume = models.Resume(
        student_id=resume.student_id,
        description=resume.description
    )
    db.session.add(db_resume)
    db.session.commit()
    return db_resume


@app.get("/resumes")
def get_resumes():
    resumes = db.session.query(models.Resume).all()

    return resumes


@app.get("/resume/{resume_id}", response_model=schemas.Resume)
def get_resume(resume_id: int):
    resume = db.session.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if resume is None:
        return JSONResponse(status_code=404, content={"message": "Resume not found"})
    return resume


@app.post("/resume/{resume_id}", response_model=schemas.Resume)
def delete_resume(resume_id: int):
    resume = get_resume(resume_id)
    db.session.delete(resume)
    db.session.commit()
    return resume


@app.post("/projects", response_model=schemas.Project)
def create_projects(project: schemas.Project):
    db_projects = models.Project(
        name=project.name,
        student_id=project.student_id,
        description=project.description
    )
    db.session.add(db_projects)
    db.session.commit()
    return db_projects


@app.get("/projects")
def get_projects():
    projects = db.session.query(models.Project).all()

    return projects


@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project(project_id: int):
    project = db.session.query(models.Project).filter(models.Project.id == project_id).first()
    if project is None:
        return JSONResponse(status_code=404, content={"message": "Project not found"})
    return project


@app.post("/project/{project_id}", response_model=schemas.Project)
def delete_project(project_id: int):
    project = get_project(project_id)
    db.session.delete(project)
    db.session.commit()
    return project


@app.post("/applications", response_model=schemas.Application)
def create_applications(application: schemas.Application):
    db_applications = models.Application(
        student_id=application.student_id,
        job_id=application.job_id
    )
    db.session.add(db_applications)
    db.session.commit()
    return db_applications


@app.get("/applications")
def get_applications():
    applications = db.session.query(models.Application).all()

    return applications


@app.get("/applications/{application_id}", response_model=schemas.Application)
def get_application(application_id: int):
    application = db.session.query(models.Application).filter(models.Application.id == application_id).first()
    if application is None:
        return JSONResponse(status_code=404, content={"message": "Application not found"})
    return application


@app.post("/applications/{application_id}", response_model=schemas.Application)
def delete_application(application_id: int):
    application = get_application(application_id)
    db.session.delete(application)
    db.session.commit()
    return application
