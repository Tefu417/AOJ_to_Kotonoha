# '入力された文字列のリストをLとする
L = list(input())
# 空列をLLとする
LL = []
# Lの各要素を順にiとして、繰り返す
for i  in L :
  # LL.append(i.upper())
  LL.append(i.upper())
# LLを文字列""で連結した文字列を出力する
print( "".join(LL) )