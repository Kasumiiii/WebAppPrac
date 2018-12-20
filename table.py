from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import api, declarative_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta
 
meta = MetaData()
Base = declarative_base() 
"""
users = Table('Users', meta,
              Column(Integer, primary_key=True, autoincrement=True),
              Column('name', String),
              Column('address', String),
              Column('addnum', String),
              Column('mail', String),
              Column('tel', String),
             )
"""
class User(Base):
    """
    Userテーブルクラス
    """
 
    # テーブル名
    __tablename__ = 'users'
 
    # 個々のカラムを定義
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    address = Column(String(100))
    addnum = Column(String(10))
    mail = Column(String(100))
    tel = Column(String(20))