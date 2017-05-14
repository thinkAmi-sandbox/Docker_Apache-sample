#!/usr/bin/python3
import cgi

# HTTPレスポンスヘッダ
print('Content-Type: text/plain;charset=utf-8')
print('')

form = cgi.FieldStorage()
upload_file = form['upload_file']
print(upload_file)
# => FieldStorage('upload_file', 'upload_file.txt', b'\xe3\x81\x82\na')

print(dir(upload_file))
# => ['FieldStorageClass', '_FieldStorage__file', '_FieldStorage__write', '__bool__', 
#     '__class__', '__contains__', '__del__', '__delattr__', '__dict__', '__dir__', 
#     '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattr__',
#     '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#     '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__',
#     '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
#     '__subclasshook__', '__weakref__', '_binary_file', 'bufsize', 'bytes_read', 
#     'disposition', 'disposition_options', 'done', 'encoding', 'errors', 'file', 
#     'filename', 'fp', 'getfirst', 'getlist', 'getvalue', 'headers', 'innerboundary',
#     'keep_blank_values', 'keys', 'length', 'limit', 'list', 'make_file', 'name', 
#     'outerboundary', 'qs_on_post', 'read_binary', 'read_lines', 'read_lines_to_eof', 
#     'read_lines_to_outerboundary', 'read_multi', 'read_single', 'read_urlencoded', 
#     'skip_lines', 'strict_parsing', 'type', 'type_options']

print(upload_file.name)
# => upload_file

print(upload_file.filename)
# => upload_file.txt

print(upload_file.file)
#=> <_io.BytesIO object at 0x7fe34bba03b8>

# with文にも対応しているとのことなので、試してみる
# http://docs.python.jp/3/library/cgi.html
with upload_file as f:
    content = b''
    while True:
        # 1バイトずつ読み込む場合
        byte_strings = f.file.read(1)
        print(byte_strings)
        # => b'\xe3', b'\x81', b'\x82', b'\n', b'a', b'' の順に読み込まれる

        if not byte_strings:
            break
        content += byte_strings

print(content.decode('utf-8'))
# あ
# a