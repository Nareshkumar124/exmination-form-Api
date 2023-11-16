from fastapi import FastAPI
from .routers import student,department,authentication

app=FastAPI(
    docs_url='/',
    title="Exam Fee API."
)
app.include_router(student.router)
app.include_router(department.router)
app.include_router(authentication.router)



    