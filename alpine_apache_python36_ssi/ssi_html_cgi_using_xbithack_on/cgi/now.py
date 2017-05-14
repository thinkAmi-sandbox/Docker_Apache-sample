#!/usr/bin/python3

import datetime

# HTTPヘッダ
# SSIで「include virtual」する時はHTTPヘッダが必要
print('Content-Type: text/plain;charset=utf-8')
print('')

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    pass