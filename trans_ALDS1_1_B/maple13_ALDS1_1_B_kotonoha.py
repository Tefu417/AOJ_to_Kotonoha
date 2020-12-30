# fractionsモジュールを用いる
import fractions
# map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
m,n = map(int,input().split())
# fractions.gcd(m,n)をansとする
ans = fractions.gcd(m,n)
# ansを出力する
print(ans)