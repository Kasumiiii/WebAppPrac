from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from student import Student, Base

engine = create_engine('mysql+pymysql://root@localhost/test?charset=utf8')

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def create_all():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_all()