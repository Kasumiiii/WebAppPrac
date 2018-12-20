#リスト型とタプル    順序つき
#集合型             順序なし、重複を許さない
#辞書型             キーと値でデータ管理

"""
#リスト型とタプル
"""

#リスト型
#l = [40, 50]
# print(l[0])   #0番目のデータ表示
# print(len(l)) #データの個数表示
# l.append(100) #末尾にデータ追加
# print(l)      #データすべて表示

# for i in l:
#     print(i)  #繰り返し終わるまでi番目のリストの中身表示

# for i, j in enumerate(l): #何番目かまで取り出す
#     print("{0}: {1}".format(i,j))

#タプル→値の変更ができない
# items = (50, "apple", 32.5)
# print(items[1])
# #items[1] = "orange"    #タプルは上書きができないのでエラー
# print(list(items))

#スライス
# scores = [4,5,6,7,8]
# print(scores[1:4])  #5,6,7
# print(scores[:2])   #4,5
# print(scores[3:])   #7,8
# print(scores[-3:])  #6,7,8

# s = "hello"
# print(s[1:4])   #ell

"""
#セット(集合型)
"""
# a = set([5,4,8,5])
# a = {5,3,8,5}   #重複が許されないので頭の５が消える
# print(a)
# print(5 in a) #true
# a.add(2)    #データの追加
# a.remove(3) #データの削除
# print(a)
# print(len(a))

# a = {1,3,5,8}
# b = {3,5,8,9}
# print (a | b)   #or {1, 3, 5, 8, 9}
# print (a & b)   #and {8, 3, 5}
# print (a - b)   #   {1}

"""
辞書型
"""

sales = {"taguchi":200, "fkoji":400}    #キーと値を定義
# print(sales["taguchi"])     #キーを指定すれば値が呼び出される
# sales["taguchi"] = 300      #キーを指定して値を変更
# sales["dot"] = 500          #キーと値の追加
# del(sales["fkoji"])         #キーを削除(値も一緒に削除)
# print(sales)

for key, value in sales.items():
    print("{0}: {1}".format(key, value)) #キーと値がそれぞれkey,valueに入る