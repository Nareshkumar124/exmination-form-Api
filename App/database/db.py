from sqlalchemy import create_engine,Engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker,Session
from dotenv import load_dotenv
import os
load_dotenv()


class Base(DeclarativeBase):
    pass

engine: Engine=create_engine(url=os.getenv('DATABASE_URL'),echo=True)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db: Session=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    




