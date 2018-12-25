from table import User
from db_util import get_session
from sqlalchemy import or_

session = get_session()
user = User()

class DBcnt:
    def __init__(self):
        pass
    
    def add_data(self, val_data):

        if len(val_data) > 1:
            user.name = val_data[0]
            user.address = val_data[1]
            user.addnum = val_data[2]
            user.mail = val_data[3]
            user.tel = val_data[4]

            session.add(user)
            session.commit()

        users = session.query(User).all()

        for user_object in users:
            # print(f'{user_object.user_id} : {user_object.name}')
            print(f'{user_object.user_id} : {user_object.name}, {user_object.address}, {user_object.addnum}, {user_object.mail}, {user_object.tel}')


#検索
    def show_data(self):
        users = session.query(User).all()
        return users

    def search_data(self, key):
        print(key)
        users = session.query(User).filter(or_(User.name==key, User.address==key, User.addnum==key, User.mail==key, User.tel==key)).all()
        for user_object in users:
            # print(f'{user_object.user_id} : {user_object.name}')
            print(f'{user_object.user_id} : {user_object.name}, {user_object.address}, {user_object.addnum}, {user_object.mail}, {user_object.tel}')
        return users

    def detail_data(self, key):
        target = session.query(User).filter(User.user_id==key).all()
        return target

session.close()