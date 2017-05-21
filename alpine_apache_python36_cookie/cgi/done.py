#!/usr/bin/python3

from http.cookies import SimpleCookie
import os

# HTTPレスポンスヘッダ
print('Content-Type: text/plain;charset=utf-8')
print('')

# レスポンスボディ
# 環境変数にセットされたCookieを表示する
env_cookie = os.environ.get('HTTP_COOKIE')
print('environ ver:')
print(env_cookie)
print('-'*20)

# SimpleCookieを使って表示する
print('SimpleCookie ver:')
cookie = SimpleCookie(env_cookie)
print(type(cookie))
print(cookie)
