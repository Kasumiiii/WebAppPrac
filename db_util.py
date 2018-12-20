from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table import User, Base

url = 'mysql+pymysql://root@localhost/test?charset=utf8'
engine = create_engine(url, echo=True)

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

#新規にテーブルを作成する場合
"""
def create_all():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_all()
"""