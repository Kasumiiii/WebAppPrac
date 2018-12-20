import re

#クラス名は最初が大文字になります。
class Validator:
    print('class validator')
    #これはコンストラクタです。
    def __init__(self):
        print('validator init') 
        self._compile = re.compile(r'^\d+$')

    #クラスのメソッド定義には、必ず第一引数をselfにする必要があります。
    #また、メンバ変数はselfがつきます。Javaでいうところのプライベート変数には慣習的に_をつけます。
    #なお、メソッドを呼び出すときには、method(self)のようにしなくても大丈夫です。
    def validate(self, target):
        print('validator validate')
        if not self._compile.match(target):
            return '数字を入力してください'
        
        value = int(target)
        if value > 120 or value < 3:
            return '年齢の数値が不正です'
        return False 
