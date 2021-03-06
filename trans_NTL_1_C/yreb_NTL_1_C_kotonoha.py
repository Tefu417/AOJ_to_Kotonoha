# 入力された文字列の整数値をnとする
n = int(input())
# 入力された文字列を空白で分割した列をLとする
L = input().split( )
# {{'0からn未満までの数列}}の各要素をiとし、L(i)の整数値の列をaとする
a = [int(L[i]) for i in range(n)]
# '0からnから1を引いた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n-1) :
  # a(i)をxとする
  x = a[i]
  # a(iに1を加えた値)をyとする
  y = a[i+1]
  # xをyで割った余りが0と等しくない間、繰り返す
  while x%y!=0 :
    # yをwとする
    w = y
    # xをyで割った余りをyとする
    y = x%y
    # wをxとする
    x = w
  # a({{iに1を加えた値}})にa(i)を掛けた値をyで割った商をa[i+1]にする
  a[i+1] = a[i+1]*a[i]//y
# a({{nから1を引いた値}})を出力する
print(a[n-1])