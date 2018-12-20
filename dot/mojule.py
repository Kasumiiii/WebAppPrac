#モジュール
#import mypackage.user as mymodule
from mypackage.user import AdminUser

bob = AdminUser("bob", 23)

print(bob.name)
bob.say_hi()
bob.say_hello()