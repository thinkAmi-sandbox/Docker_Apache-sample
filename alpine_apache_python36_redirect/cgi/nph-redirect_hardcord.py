#!/usr/bin/python3

# HTTPレスポンスヘッダ
# NPHなので、ステータスラインも記述する
print('HTTP/1.1 302 Found')
print('Location: /cgi-bin/done_redirect.py')
print('Server: hoge')
print('')
