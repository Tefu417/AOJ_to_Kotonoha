# 入力された文字列をsとする
s = input()
# sの各要素を順にiとして、繰り返す
for i  in s :
  # iの全てが英大文字のとき、
  if i.isupper() :
    # iを英小文字に変換した文字列と((end, ''))からなる辞書を出力する
    print(i.lower(), end='')
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#MethodExpr recv: [#Name 'i']name: [#Name 'upper']params: [#Arguments '']][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]
# 空行を出力する
print()