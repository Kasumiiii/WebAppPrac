#イテレータ

# scores = [40,50,70,90,60]
# it = iter(scores)
# print(next(it))
# print(next(it))
# print("hello")
# print(next(it))

# def get_infinite():
#     i = 0
#     while True: #無限ループ
#         yield i*2   #次の要素を引っ張ってくる
#         i += 1

# g = get_infinite()
# print(next(g))
# print(next(g))
# print(next(g))

"""
map(関数, イテレータ)
"""
# def triple(n):
#     return n*3

# print(list(map(triple, [1,2,3])))

#filter(関数,イテレータ)
#条件に合致した

# def is_even(n):
#     return n%2 == 0

# print(list(filter(is_even, range(10))))
print(list(filter(lambda n: n%2 ==0, range(10))))
