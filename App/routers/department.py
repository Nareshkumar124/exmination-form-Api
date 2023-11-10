from fastapi import APIRouter,Body,Depends,HTTPException,status
from pydantic import  BaseModel
from typing import Annotated
from ..database.db import get_db
from ..database.modals import *
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

router=APIRouter(
    prefix='/departments',
    tags=['department']
)



@router.get('/')
async def allDepartment(db:Session=Depends(get_db)):
    try:
        return db.query(Department).all()
    except Exception:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="Data Not found")
    