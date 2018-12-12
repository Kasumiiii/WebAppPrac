from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, MetaData
from sqlalchemy import create_engine
 
meta = MetaData()
url = 'mysql+pymysql://root@localhost/test?charset=utf8'
engine = create_engine(url, echo=True)
Base = declarative_base() 

users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('add', String),
              Column('addnum', String),
              Column('mail', String),
              Column('tel', String),
             )
 
class User(Base):
    """
    Userテーブルクラス
    """
 
    # テーブル名
    __tablename__ = 'users'
 
    # 個々のカラムを定義
    id = Column(Integer, primary_key=True)
    name = Column(String)
    add = Column(String)
    addnum = Column(String)
    mail = Column(String)
    tel = Column(String)
