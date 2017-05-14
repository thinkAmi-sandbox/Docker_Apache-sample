#!/usr/bin/python3
# shebangに指定するPython3を以下で確認
# bash-4.3# which python3
# /usr/bin/python3

import os
import sys

# HTTPレスポンスヘッダ
print('Content-Type: text/plain;charset=utf-8')
print('')

# HTTPレスポンスボディ
# Apacheでは標準入力と環境変数を使ってブラウザとサーバがデータのやり取りをするため、
# それらをHTTPレスポンスボディとして表示してみる
# http://httpd.apache.org/docs/current/howto/cgi.html#behindscenes

# 標準入力
print('-'*20)
print('stdin:\n{}'.format(sys.stdin.read()))

# 環境変数
print('-'*20)
print('os.environ:\n')
for k, v in os.environ.items():
    print('{}: {}'.format(k, v))