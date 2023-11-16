from fastapi import APIRouter, Body, Path, Response, Depends,HTTPException,status
from pydantic import BaseModel
from typing import Annotated
from ..database.db import get_db
from ..database.modals import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

router = APIRouter(prefix="/student", tags=["student"])

class std(BaseModel):
    auid: str
    department: str
    course: str
    sem: int


class std2(std):
    ...


# 67890
@router.get("/detail/{auid}")
async def getStudenDetail(auid: Annotated[str, Path()], db: Session = Depends(get_db)):
    try:
        studentData: Student = db.query(Student).filter(Student.auid == auid).one()
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data not found")
    return studentData


@router.post('/')
async def studentData(stdData:std,db: Session = Depends(get_db)):
    coloumn=select(Student.firstName,Student.lastName,Department.departmentName).where(Student.auid==stdData.auid)
    data=db.execute(coloumn)
    for i in data:
        return list(i)
    