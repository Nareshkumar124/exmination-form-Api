from fastapi import FastAPI
from .routers import student,department

app=FastAPI(
    docs_url='/',
    title="Exam Fee API."
)
app.include_router(student.router)
app.include_router(department.router)



    