[#Document [# '-*- coding: utf-8 -*-']]
# [#MultiString '"\nhttp://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_A&lang=jp\n\n"']
"
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_A&lang=jp

"
# sysモジュールを用いる
import sys[#FromDecl name: [#ModuleName 'sys']names: [# [#Name 'stdin']]]
# stdin.readlineをinputとする
input = stdin.readline
# 関数mainを[#FuncParam [#ParamDecl name: [#Name 'args']]]のパラメータを持つように定義する
def main (args) :
  # 入力された文字列の両端から空白改行を取り除いた文字列をsとする
  s = input().strip()
  # sの英大文字を英小文字、英小文字を英大文字に変換した文字列をtoggledとする
  toggled = s.swapcase()
  # toggledを出力する
  print(toggled)
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # main(sys.argvの先頭を除いた部分)
  main(sys.argv[1:])