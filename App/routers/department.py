from fastapi import APIRouter,Body,Depends
from pydantic import  BaseModel
from typing import Annotated
from ..database.db import get_db
from ..database.modals import *
from sqlalchemy.orm import Session

router=APIRouter(
    prefix='/departments',
    tags=['department']
)



@router.get('/')
async def allDepartment(db:Session=Depends(get_db)):
    res={"departments":[]}
    for i in db.query(Department).all():
        data={
            "department_id":i.departmentID,
            "department_name":i.departmentName
        }
        res['departments'].append(data)
    return res
    