class Model:
    print('class model') 
    def __init__(self):
        print('model init')
        pass #コンストラクタが必要ないときは__init__は特に書く必要はありません。

    def save(self, value):
        print('model save')
        print(f'{value}歳を保存しました')
        #上記のテクニックはf-stringといいます。
