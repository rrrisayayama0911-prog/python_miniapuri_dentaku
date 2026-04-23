# 2つの数字を足し算する

"""
while True:

    try:
        a = int(input("1つ目の数字："))
        b = int(input("2つ目の数字："))
        break

    except ValueError:
        print("数字を入力してね:")

result = a + b
print("結果：", result)


"""

while True:
    try:

        #inputは文字列より、int()関数で数値や文字列を整数型に変換する
        a=int(input("1つ目の数字："))
        b=int(input("2つ目の数字："))
        break
    except ValueError:
        print("数字を入力してね")

result=a+b
print("結果",result)


