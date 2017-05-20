#!/usr/bin/python3

import os
# ステータスコードとメッセージはPythonの定数を使う
# https://docs.python.jp/3/library/http.html
from http import HTTPStatus

# CGIの環境変数からプロトコルとバージョン・ホストを取得する
protocol = os.environ.get('SERVER_PROTOCOL')
server = os.environ.get('SERVER_SOFTWARE')

# HTTPレスポンスヘッダ
print(f'{protocol} {HTTPStatus.FOUND.value} {HTTPStatus.FOUND.phrase}')
print('Location: /cgi-bin/done_redirect.py')
print(f'Server: {server}')
print('')