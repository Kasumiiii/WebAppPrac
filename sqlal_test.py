from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'mysql+pymysql://root@localhost/test?charset=utf8'
engine = create_engine(url, echo=True)
Base = declarative_base()

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	name = Column(String(50))

	def __repr__(self):
       	 return "<User(name='%s')>" % (self.name)

Base.metadata.create_all(engine)

u1= User(name='hawk')
Session = sessionmaker(bind=engine)
session = Session()
for i in session.query(User).order_by(User.id):
    print(i.name)
