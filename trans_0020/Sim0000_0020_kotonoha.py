# 'abcdefghijklmnopqrstuvwxyz'をaとする
a = 'abcdefghijklmnopqrstuvwxyz'
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'をAとする
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# input().translate(str.maketrans(a, A))を出力する
print(input().translate(str.maketrans(a, A)))