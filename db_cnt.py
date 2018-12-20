from table import User
from db_util import get_session

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
            print(f'{user_object.user_id} : {user_object.name}')

#検索
"""
target = session.query(User).filter(User.name=="tanaka").first()
target.name = 'yamada'
session.commit()
"""

session.close()