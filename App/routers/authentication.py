from fastapi import APIRouter, Body, Path,Form, Response, Depends,HTTPException,status,Response
from pydantic import BaseModel
from typing import Annotated
from ..database.db import get_db
from ..database.modals import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

router = APIRouter(prefix="/authentication", tags=["authentication"])



class AUT(BaseModel):
    auid:str
    password:str

@router.post("/")
async def getCredentials(auid:Annotated[str,Form()],password:Annotated[str,Form()],response:Response,db:Session=Depends(get_db)):
    selectData=select(Student.firstName,Student.lastName).where(Student.auid==auid ).where(Student.password==password)
    dataOfUser=db.execute(selectData)
    dataFromDataBase=dataOfUser.first()
    print(dataFromDataBase)
    if not dataFromDataBase:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User is not available.")
    response.set_cookie('auid',auid)
    returnObject={
        "first_name":dataFromDataBase[0],
        "last_name":dataFromDataBase[1]
    }
    
        
    return returnObject