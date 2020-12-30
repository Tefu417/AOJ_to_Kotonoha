# sysモジュールを用いる
import sys
# 2000000000をBIG_NUMとする
BIG_NUM = 2000000000
# 1000000007をMODとする
MOD = 1000000007
# 0.000000001をEPSとする
EPS = 0.000000001
# 入力された文字列の文字列をbufとする
buf = str(input())
# bufの英大文字を英小文字、英小文字を英大文字に変換した文字列を出力する
print(buf.swapcase())