#!/usr/bin/python3
import cgi

# HTTPレスポンスヘッダ
print('Content-Type: text/plain;charset=utf-8\n')
print('')

form = cgi.FieldStorage()
print(form)
# => FieldStorage(None, None, [FieldStorage('upload_file', 'upload_file.txt', b'\xe3\x81\x82\na')])

# 一気に読み込む場合
content = form.getvalue('upload_file')

print(content.__class__)
# => <class 'bytes'>

# バイト文字列なので、decodeして読めるようにする
print(content.decode('utf-8'))
# =>
# あ
# a