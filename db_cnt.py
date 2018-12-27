from table import User
from db_util import get_session
from sqlalchemy import or_

session = get_session()
user = User()

class DBcnt:
    def __init__(self):
        pass
    
    #データ追加
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

        # for user_object in users:
        #     print(f'{user_object.user_id} : {user_object.name}, {user_object.address}, {user_object.addnum}, {user_object.mail}, {user_object.tel}')
    
    #データ一覧表示
    def show_data(self):
        users = session.query(User).all()
        return users

    #データ検索
    def search_data(self, key):
        # print(key)
        users = session.query(User).filter(or_(User.name==key, User.address==key, User.addnum==key, User.mail==key, User.tel==key)).all()
        # for user_object in users:
        #     print(f'{user_object.user_id} : {user_object.name}, {user_object.address}, {user_object.addnum}, {user_object.mail}, {user_object.tel}')
        return users

    #データ詳細
    def detail_data(self, key):
        target = session.query(User).filter(User.user_id==key).all()
        return target

    #データアップデート
    def update_data(self, updata):
        target = session.query(User).filter(User.user_id==updata[5]).all()
        target.name = updata[0]
        target.address = updata[1]
        target.addnum = updata[2]
        target.mail = updata[3]
        target.tel = updata[4]

        session.commit()
        return target

    #データ削除
    def delete_data(self, key):
        session.query(User).filter(User.user_id==key).delete()
        session.commit()

session.close()