# 入力された文字列をstrとする
str = input()
# strの各要素を順にsとして、繰り返す
for s  in str :
  # sの全てが英大文字のとき、
  if s.isupper() :
    # sを英小文字に変換した文字列と((end, ''))からなる辞書を出力する
    print(s.lower(), end='')
  # ('sの全てが英小文字の',)
  elif s.islower() :
    # sを英大文字に変換した文字列と((end, ''))からなる辞書を出力する
    print(s.upper(), end='')
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 's'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]
# 空行を出力する
print()