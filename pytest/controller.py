from validator import Validator
from model import Model
#importする場合は、from ファイル名 import クラス名とします。
#これは同一フォルダの場合だけで、別フォルダの場合はいろいろとややこしいルールがあります。
#また、クラスに限らずメソッドや定数もimportできます。

class Controller:
    print('class controller')
    def __init__(self, answer):
        print('cont init')
        self._answer = answer.strip()

    def do_something(self):
        print('cont something')
        validator = Validator()
        result = validator.validate(self._answer)
        if result != False:
            return result
        else:
            sql_alchemy_object = Model()
            sql_alchemy_object.save(self._answer)
        return '処理を正常に終了しました。'

