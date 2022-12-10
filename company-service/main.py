from fastapi import FastAPI
from config import engine
import models
import router
import os
import uvicorn

from schemas import CompanySchema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


"""@app.post("/add-company/", response_model=CompanySchema)
def add_company(company: CompanySchema):
    db_company = ModelCompany(title=company.name)"""

#app.include_router(router, prefix="/company", tags=["company"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
