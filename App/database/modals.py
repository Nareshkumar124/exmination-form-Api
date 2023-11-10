from .db import Base,engine
from sqlalchemy import ForeignKey,Integer,Boolean,String,Column
from sqlalchemy.types import DATE
import uuid

class Student(Base):
    __tablename__='student'
    auid=Column('auid',String,primary_key=True)
    password=Column('password',String,nullable=False)
    firstName=Column('first_name',String,nullable=False)
    lastName=Column('last_name',String,nullable=False)
    image=Column('image',String,nullable=False)
    fatherName=Column('father_name',String,nullable=False)
    motherName=Column('mother_name',String,nullable=False)
    address=Column('address',String,nullable=False)
    phoneNumber=Column('phone_number',String,nullable=False)
    email=Column('email',String)
    semester=Column('semester',Integer,nullable=False)
    programID=Column('program_id',Integer,ForeignKey('program.program_id'))
    

class Department(Base):
    __tablename__='department'
    departmentID=Column('department_id',String,primary_key=True,default=uuid.uuid4())
    departmentName=Column('department_name',String,nullable=False)
    
class Program(Base):
    __tablename__='program'
    programID=Column('program_id',Integer,primary_key=True)
    programName=Column('program_name',String,nullable=False)
    duration=Column('duration',Integer,nullable=False)
    departmentID=Column('department_id',String,ForeignKey('department.department_id'))
    

class Receipt(Base):
    __tablename__='receipt'
    receiptNumber=Column('receipt_number',String,primary_key=True)
    auid=Column('auid',String,ForeignKey('student.auid'))
    fees=Column('fees',Integer,nullable=False)
    date=Column('date',DATE,nullable=False)
    regular=Column('regular',Boolean,nullable=False,default=True)
    
class ReceiptRe(Base):
    __tablename__='receipt_re'
    receiptNumber=Column('receipt_number',String,primary_key=True)
    auid=Column('auid',String,ForeignKey('student.auid'))
    fees=Column('fees',Integer,nullable=False)
    date=Column('date',DATE,nullable=False)
    subjectCode=Column('subject_code',String,ForeignKey('subject.subject_code'))

class Subject(Base):
    __tablename__='subject'
    subjectCode=Column('subject_code',String,primary_key=True)
    subjectName=Column('subject_name',String,nullable=False)
    
class ProgramAndSubject(Base):
    __tablename__='program_and_subject'
    key=Column('key',Integer,autoincrement=True,primary_key=True)
    programID=Column('program_id',Integer,ForeignKey('program.program_id'))
    semester=Column('semester',Integer,nullable=False)
    subjectCode=Column('subject_code',String,ForeignKey('subject.subject_code'))

class PreviousResult(Base):
    __tablename__='previous_result'
    id=Column('id',Integer,primary_key=True,autoincrement=True)
    auid=Column('auid',String,ForeignKey('student.auid'))
    receiptNumber=Column('receipt_number',String,ForeignKey('receipt.receipt_number'))
    examination=Column('examination',String,nullable=False)
    board=Column('board',String,nullable=False)
    session=Column('session',DATE,nullable=False)
    rollNo=Column('roll_no',String,nullable=False)
    passFail=Column('pass_fail',Boolean,nullable=False)
    reAppear=Column('re_appear',Boolean,nullable=False)
    
class PreviousSubject(Base):
    __tablename__='previous_subject'
    previousYearSubjectID=Column('previous_year_subject_id',Integer,autoincrement=True,primary_key=True)
    id=Column('id',Integer,ForeignKey('previous_result.id'))
    subjectName=Column('subject_name',String)
    

# Base.metadata.create_all(bind=engine)
    