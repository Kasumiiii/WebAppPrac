from controller import Controller

age = input('何歳ですか？ : ')

#クラスを使うには、インスタンス化しなければいけません
#Javaでいうところのnew()みたいなものです。
print('1')
controller = Controller(age) 
print('2')
result = controller.do_something()
print(result)

