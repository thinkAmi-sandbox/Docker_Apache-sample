#!/usr/bin/python3

# HTTPレスポンスヘッダ
import os
# ステータスコードとメッセージはPythonの定数を使う
# https://docs.python.jp/3/library/http.html
from http import HTTPStatus
from http.cookies import SimpleCookie

# CGIの環境変数からプロトコルとバージョンを取得する
protocol = os.environ.get('SERVER_PROTOCOL')

# HTTPレスポンスヘッダ
# NPHなので、ステータスラインも記述する
print(f'{protocol} {HTTPStatus.FOUND.value} {HTTPStatus.FOUND.phrase}')
print('Location: /cgi-bin/done.py')

# Cookie
cookie = SimpleCookie()
cookie['foo'] = 'bar'
cookie['foo']['httponly'] = True
cookie['hoge'] = 'fuga'

print(cookie.output())
print('')

