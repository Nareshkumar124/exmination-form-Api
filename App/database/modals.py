from .db import Base,engine
from sqlalchemy import ForeignKey,Integer,Boolean,String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.types import DATE
import uuid

class Student(Base):
    __tablename__='student'
    auid:Mapped[str]=mapped_column('auid',String,primary_key=True)
    firstName:Mapped[str]=mapped_column('first_name',String,nullable=False)
    lastName:Mapped[str]=mapped_column('last_name',String,nullable=False)
    image:Mapped[str]=mapped_column('image',String,nullable=False)
    fatherName:Mapped[str]=mapped_column('father_name',String,nullable=False)
    motherName:Mapped[str]=mapped_column('mother_name',String,nullable=False)
    address:Mapped[str]=mapped_column('address',String,nullable=False)
    phoneNumber:Mapped[str]=mapped_column('phone_number',String,nullable=False)
    email:Mapped[str]=mapped_column('email',String)
    semester:Mapped[int]=mapped_column('semester',Integer,nullable=False)
    programID:Mapped[int]=mapped_column('program_id',Integer,ForeignKey('program.program_id'))
    

class Department(Base):
    __tablename__='department'
    departmentID:Mapped[str]=mapped_column('department_id',String,primary_key=True,default=uuid.uuid4())
    departmentName:Mapped[str]=mapped_column('department_name',String,nullable=False)
    
class Program(Base):
    __tablename__='program'
    programID:Mapped[int]=mapped_column('program_id',Integer,primary_key=True)
    programName:Mapped[str]=mapped_column('program_name',String,nullable=False)
    duration:Mapped[int]=mapped_column('duration',Integer,nullable=False)
    departmentID:Mapped[str]=mapped_column('department_id',String,ForeignKey('department.department_id'))
    

class Reciept(Base):
    __tablename__='reciept'
    recieptNumber:Mapped[str]=mapped_column('reciept_number',String,primary_key=True)
    auid:Mapped[str]=mapped_column('auid',String,ForeignKey('student.auid'))
    fees:Mapped[int]=mapped_column('fees',Integer,nullable=False)
    date:Mapped[DATE]=mapped_column('date',DATE,nullable=False)
    regular:Mapped[bool]=mapped_column('regualar',Boolean,nullable=False,default=True)
    
class RecieptRe(Base):
    __tablename__='reciept_re'
    recieptNumber:Mapped[str]=mapped_column('reciept_number',String,primary_key=True)
    auid:Mapped[str]=mapped_column('auid',String,ForeignKey('student.auid'))
    fees:Mapped[int]=mapped_column('fees',Integer,nullable=False)
    date:Mapped[DATE]=mapped_column('date',DATE,nullable=False)
    subjectCode:Mapped[str]=mapped_column('subject_code',String,ForeignKey('subject.subject_code'))

class Subject(Base):
    __tablename__='subject'
    subjectCode:Mapped[str]=mapped_column('subject_code',String,primary_key=True)
    subjectName:Mapped[str]=mapped_column('subject_name',String,nullable=False)
    
class ProgramAndSubject(Base):
    __tablename__='program_and_subject'
    key:Mapped[int]=mapped_column('key',Integer,autoincrement=True,primary_key=True)
    programID:Mapped[int]=mapped_column('program_id',Integer,ForeignKey('program.program_id'))
    semester:Mapped[int]=mapped_column('semester',Integer,nullable=False)
    subjectCode:Mapped[str]=mapped_column('subject_code',String,ForeignKey('subject.subject_code'))
    

# Base.metadata.create_all(bind=engine)
    