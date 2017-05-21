#!/usr/bin/python3

# HTTPレスポンスヘッダ
import os
# ステータスコードとメッセージはPythonの定数を使う
# https://docs.python.jp/3/library/http.html
from http import HTTPStatus

# CGIの環境変数からプロトコルとバージョンを取得する
protocol = os.environ.get('SERVER_PROTOCOL')

# HTTPレスポンスヘッダ
# NPHなので、ステータスラインも記述する
print(f'{protocol} {HTTPStatus.FOUND.value} {HTTPStatus.FOUND.phrase}')
print('Location: /cgi-bin/done.py')
print('Set-Cookie: foo=bar; HttpOnly;')
print('Set-Cookie: hoge=fuga')
print('')
