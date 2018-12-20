#例外処理

class MyException(Exception):
    #pythonがあらかじめ用意しているexceptionクラスを継承
    #独自の例外等をつくれる
    pass

def div(a,b):
    try:
        if b < 0:
            raise MyException("not minus")
        print(a / b)
    except ZeroDivisionError:
        print("not by zero!")
    except MyException as e:
        print(e)
    else:
        print("no exception")
    finally:
        print("--end--")

div(10, 0)
div(10, -1)
div(10, 2)