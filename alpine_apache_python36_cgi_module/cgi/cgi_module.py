#!/usr/bin/python3
import cgi
import sys
import os

# HTTPレスポンスヘッダ
print('Content-Type: text/plain;charset=utf-8')
print('')


# name, filenameはファイル関係のものなので、単なるフォームであればNoneがセットされる
# https://github.com/python/cpython/blob/master/Lib/cgi.py#L498
# form = cgi.FieldStorage()
# print(form)
# => FieldStorage(None, None, [MiniFieldStorage('quantity', '1個'), 
#                              MiniFieldStorage('hidden_valude', '隠しデータ')])

# 空の文字列を含むフォーム要素のkeyも取得したい場合は、keep_blank_values=Trueにする
form = cgi.FieldStorage(keep_blank_values=True)
print(form)
# => FieldStorage(None, None, [MiniFieldStorage('subject', ''), 
#                              MiniFieldStorage('quantity', '1個'), 
#                              MiniFieldStorage('hidden_valude', '隠しデータ'), 
#                              MiniFieldStorage('memo', '')])
# 未選択のcheckboxやradio button、select multipleは取得できない模様
# (selectは取得できている)

re_instance = cgi.FieldStorage()
print(re_instance)


print(form.type)
# => application/x-www-form-urlencoded

print(form.headers)
# => {'content-type': 'application/x-www-form-urlencoded', 'content-length': '94'}


# 要素まわり

print(form.keys())
# => ['quantity', 'memo', 'hidden_valude', 'subject']


# 「自分で持ち帰る」チェックボックスにチェックを入れた場合
print(form['takeout'])
# => MiniFieldStorage('takeout', '自分で持ち帰る')

print(form['takeout'].value)
# => 自分で持ち帰る

print(form.getlist('takeout'))
# => ['自分で持ち帰る']


# 色々な方法で存在しないnameを指定してみる
try:
    print(form['foo'])
except:
    print('not found: foo')
# => 例外が出て、「not found: foo」のみ表示

print(form.getvalue('foo'))
# => None
print(form.getvalue('foo', 'default_value'))
# => default_value


# 同じnameを持つ、複数のcheckboxにチェックを入れた場合
print(form.getfirst('purpose'))
# => 贈り物にする

print(form.getlist('purpose'))
# => ['贈り物にする', '自家用にする']


# 標準入力
print('stdin:\n{}'.format(sys.stdin.read()))
# => cgi.FieldStorageでsys.stdinを読み込んでいるので、その後だと何も読み取れない

# 環境変数
print('os.environ:\n')
for k, v in os.environ.items():
    print('{}: {}'.format(k, v))
    # => こちらは標準入力とは異なり、FieldStorage()したあとでも値を取得できる

# HTTP_HOST: localhost:8081
# HTTP_CONNECTION: keep-alive
# CONTENT_LENGTH: 292
# HTTP_CACHE_CONTROL: max-age=0
# HTTP_ORIGIN: http://localhost:8081
# HTTP_UPGRADE_INSECURE_REQUESTS: 1
# HTTP_USER_AGENT: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
# CONTENT_TYPE: application/x-www-form-urlencoded
# HTTP_ACCEPT: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# HTTP_REFERER: http://localhost:8081/form_post_cgi.html
# HTTP_ACCEPT_ENCODING: gzip, deflate, br
# HTTP_ACCEPT_LANGUAGE: ja,en-US;q=0.8,en;q=0.6
# PATH: /usr/local/apache2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# SERVER_SIGNATURE: 
# SERVER_SOFTWARE: Apache/2.4.25 (Unix)
# SERVER_NAME: localhost
# SERVER_ADDR: 172.17.0.2
# SERVER_PORT: 8081
# REMOTE_ADDR: 172.17.0.1
# DOCUMENT_ROOT: /usr/local/apache2/htdocs
# REQUEST_SCHEME: http
# CONTEXT_PREFIX: /cgi-bin/
# CONTEXT_DOCUMENT_ROOT: /usr/local/apache2/cgi-bin/
# SERVER_ADMIN: you@example.com
# SCRIPT_FILENAME: /usr/local/apache2/cgi-bin/cgi_module.py
# REMOTE_PORT: 59686
# GATEWAY_INTERFACE: CGI/1.1
# SERVER_PROTOCOL: HTTP/1.1
# REQUEST_METHOD: POST
# QUERY_STRING: 
# REQUEST_URI: /cgi-bin/cgi_module.py
# SCRIPT_NAME: /cgi-bin/cgi_module.py