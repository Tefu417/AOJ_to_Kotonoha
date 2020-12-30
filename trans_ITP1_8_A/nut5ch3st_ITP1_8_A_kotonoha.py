# 入力された文字列を','で分割した列をarrayとする
array = input().split(',')
# arrayの各要素をaryとし、{{aryの英大文字を英小文字、英小文字を英大文字に変換した文字列}}の列をansとする
ans = [ary.swapcase() for ary in array]
# ansを文字列','で連結した文字列を出力する
print(','.join(ans))