# {{入力された文字列の各要素をcとし、(c.upper()とc.lower())からなる列({{cの全てが英大文字かどうか}})の列}}を文字列''で連結した文字列を出力する
print(''.join([c.upper(), c.lower()][c.isupper()] for c in input()))