from http.cookies import SimpleCookie, Morsel
from email.utils import formatdate # for expires (RFC1123)
import inspect


COOKIE_STR = 'foo=ham; bar=spam'

def create_cookie(is_value_only=True):
    cookie = SimpleCookie()
    cookie['foo'] = 'ham'
    if is_value_only:
        return cookie
    cookie['foo']['path'] = '/bar/baz'
    cookie['foo']['domain'] = 'example.com'
    # RFC1123形式でexpiresを設定する
    # https://triple-underscore.github.io/RFC6265-ja.html#section-4.1.1
    # http://stackoverflow.com/questions/225086/rfc-1123-date-representation-in-python
    cookie['foo']['expires'] = formatdate(timeval=None, localtime=False, usegmt=True)
    cookie['foo']['max-age'] = 100
    cookie['foo']['httponly'] = True
    cookie['foo']['secure'] = True
    return cookie


class TryCookie:
    def load_str_using_init(self):
        """str(HTTP_COOKIE)形式を__init__を使って読み込み"""
        # 実行中のメソッド名を知るために、inspectモジュールを使用
        # http://blog.rinka-blossom.com/python-inspect/
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = SimpleCookie(COOKIE_STR)
        print(cookie.__class__)
        # => <class 'http.cookies.SimpleCookie'>

        for key, morsel in cookie.items():
            print(morsel.__class__)
            # => <class 'http.cookies.Morsel'>
            print(morsel)
            # => Set-Cookie: foo=ham
            #    Set-Cookie: bar=spam

    def load_str_using_method(self):
        """str(HTTP_COOKIE)形式をloadを使って読み込み"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = SimpleCookie()
        cookie.load(COOKIE_STR)
        print(cookie.__class__)
        # => <class 'http.cookies.SimpleCookie'>

        for key, morsel in cookie.items():
            print(morsel.__class__)
            # => <class 'http.cookies.Morsel'>
            print(morsel)
            # => Set-Cookie: foo=ham
            #    Set-Cookie: bar=spam

    def load_dic(self):
        """dict形式を読み込み"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        data = {
            'foo': 'ham',
            'bar': 'spam',
        }
        cookie = SimpleCookie(data)
        print(cookie.__class__)
        # => <class 'http.cookies.SimpleCookie'>

        for key, morsel in cookie.items():
            print(morsel.__class__)
            # => <class 'http.cookies.Morsel'>
            print(morsel)
            # => Set-Cookie: foo=ham
            #    Set-Cookie: bar=spam

    def output_and_str(self):
        """outputと__str__を使う"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie()
        
        print(cookie.output())
        # => Set-Cookie: foo=ham
        print(cookie)
        # => Set-Cookie: foo=ham

    def output_with_quote_value(self):
        """outputした時にクォートで囲まれるもの"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        data = {
            'foo': 'ham',
            'bar': 'spam eggs',
            'baz': 'あ',
        }
        cookie = SimpleCookie(data)
        print(cookie)
        # 必要に応じてダブルクォートで囲まれる
        # ただし、日本語などはそのままセットされる
        # => Set-Cookie: bar="spam eggs"
        #   Set-Cookie: baz="あ"
        #   Set-Cookie: foo=ham

    def output_with_args_header(self):
        """output()を使う時に、引数headerを指定する場合"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie()
        print(cookie.output(header='hoge'))
        # => hoge foo=ham

    def output_with_args_sep(self):
        """output()を使う時に、引数sepを指定する場合"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        data = {
            'foo': 'ham',
            'bar': 'spam',
        }
        cookie = SimpleCookie(data)
        print(cookie.output(sep='++++'))
        # => Set-Cookie: bar=spam++++Set-Cookie: foo=ham

    def output_with_attr(self):
        """output()を使う時にCookieの属性がある場合"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie(is_value_only=False)
        print(cookie.output())
        # => Set-Cookie: foo=ham; Domain=example.com; expires=Sat, 20 May 2017 11:37:36 GMT; HttpOnly; Max-Age=100; Path=/bar/baz; Secure

    def output_by_attr_when_expires_is_str(self):
        """output()を使う時にattrsを文字列で指定する場合"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie(is_value_only=False)
        print(cookie.output(attrs='expires'))
        # => Set-Cookie: foo=ham; expires=Sat, 20 May 2017 11:39:12 GMT

    def output_by_attr_when_expires_is_list(self):
        """output()を使う時にattrsを要素1のリストで指定する場合"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie(is_value_only=False)
        print(cookie.output(attrs=['expires']))
        # => Set-Cookie: foo=ham; expires=Sat, 20 May 2017 11:39:12 GMT

    def output_by_attr_when_attrs_are_list(self):
        """output()を使う時にattrsをリストで指定する場合"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie(is_value_only=False)
        print(cookie.output(attrs=['max-age', 'httponly']))
        # => Set-Cookie: foo=ham; HttpOnly; Max-Age=100

    def js_output_with_attr(self):
        """js_output()を使う時に属性がある場合"""
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie(is_value_only=False)
        print(cookie.js_output())
        # =>
        # 
        # <script type="text/javascript">
        # <!-- begin hiding
        # document.cookie = "foo=ham; Domain=example.com; expires=Sat, 20 May 2017 11:39:12 GMT; HttpOnly; Max-Age=100; Path=/bar/baz; Secure";
        # // end hiding -->
        # </script>
        # 


class TryMorsel:
    def run_attr_and_method(self):
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        m = Morsel()
        m.set('foo', 'bar', 'baz')

        print(f'key: {m.key}')
        # => key: foo
        print(f'value: {m.value}')
        # => value: bar
        print(f'coded_value: {m.coded_value}')
        # => coded_value: baz

        print(m)
        # => Set-Cookie: foo=baz

        print(m.output())
        # => Set-Cookie: foo=baz

        print(m.OutputString())
        # => foo=baz

        print(m.js_output())
        # =>
        # <script type="text/javascript">
        # <!-- begin hiding
        # document.cookie = "foo=baz";
        # // end hiding -->
        # </script>

    def show_attr_by_created_cookie(self):
        print('[{}]:'.format(inspect.getframeinfo(inspect.currentframe())[2]))
        cookie = create_cookie()

        m = cookie.get('foo')
        print(type(m))
        # => <class 'http.cookies.Morsel'>
        
        print(f'key: {m.key}')
        # => key: foo
        print(f'value: {m.value}')
        # => value: ham
        print(f'coded_value: {m.coded_value}')
        # => coded_value: ham

if __name__ == '__main__':
    # SimpleCookieの確認
    c = TryCookie()
    c.load_str_using_init()
    print('-'*20)
    c.load_str_using_method()
    print('-'*20)
    c.load_dic()
    print('-'*20)
    c.output_and_str()
    print('-'*20)
    c.output_with_quote_value()
    print('-'*20)
    c.output_with_args_header()
    print('-'*20)
    c.output_with_args_sep()
    print('-'*20)
    c.output_with_attr()
    print('-'*20)
    c.output_by_attr_when_expires_is_str()
    print('-'*20)
    c.output_by_attr_when_expires_is_list()
    print('-'*20)
    c.output_by_attr_when_attrs_are_list()
    print('-'*20)
    c.js_output_with_attr()

    # Morselの確認
    print('-'*20)
    m = TryMorsel()
    m.run_attr_and_method()
    print('-'*20)
    m.show_attr_by_created_cookie()
