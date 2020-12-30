# sysモジュールを用いる
import sys
# 識別子が'__main__'のとき、
if __name__ == '__main__' :[#Document [# '??????????????\\???']]
  # sys.stdinの各要素を順にlineとして、繰り返す
  for line  in sys.stdin :
    # {{lineの両端から空白改行を取り除いた文字列}}を英大文字に変換した文字列を出力する
    print(line.strip().upper())