#クラスの多重継承
#a,B -> c
#同じメソッドがあった場合、先に宣言された方が優先される
class A:
    def say_a(self):
        print("A")

class B:
    def say_b(self):
        print("B")

class C(A,B):
    pass

c = C()
c.say_a()
c.say_b()