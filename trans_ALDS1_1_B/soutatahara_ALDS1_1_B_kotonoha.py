# fractionsモジュールを用いる
import fractions
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b  = map(int,input().split())
# fractions.gcd(a,b)を出力する
print(fractions.gcd(a,b))