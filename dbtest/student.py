from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import api, declarative_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

