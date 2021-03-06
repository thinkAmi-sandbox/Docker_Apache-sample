# Docker_Apache-sample

# Tested environment

- Mac OS X 10.11.6
- Docker for Mac 17.03.1-ce-mac12

　  
# Samples

- alpine_apache_python36_cgi/
  - run Apache2.4.25 + Python3.6.0 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.4
    - base Dockerfile: httpd:2.4.25-alpine, python:3.6.0-alpine
- alpine_apache_python36_cgi_form/
  - run Apache2.4.25 + Python3.6.1 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3
- alpine_apache_python36_cgi_module/
  - run Apache2.4.25 + Python3.6.1 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3
- alpine_apache_python36_ssi/
  - run Apache2.4.25 + Python3.6.1 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3
- alpine_apache_python36_redirect/
  - run Apache2.4.25 + Python3.6.1 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3
- alpine_apache_python36_cookie/
  - run Apache2.4.25 + Python3.6.1 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3
- alpine_apache_python27_mod_python
  - run Apache2.4.25 (prefork MPM) + Python2.7.13 + mod_python on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3
- alpine_apache_python3x_mod_python
  - run Apache2.4.25 (prefork MPM) + Python3.6 + mod_python on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3
- alpine_apache_prefork
  - run Apache2.4.25 (prefork MPM) on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine

　  
# License

The Unlicense.

`frolvlad/alpine-python3`'s Dockerfile, see `LICENSE_for_frol_docker-alpine-python3`.

　  
# Related Blog (Written in Japanese)

- [Dockerで、Alpine3.4 + Apache2.4.25 + Python3.6.0の環境を作って、CGIを動かしてみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/03/15/062314)
- [Dockerで、Alpine3.5 + Apache2.4 + Python3.6の環境を作って、フォームのデータをCGIで受け取ってみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/05/10/214559)
- [Docker + Alpine3.5 + Apache2.4 + Python3.6で、フォームのデータを標準モジュールcgiで受け取ってみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/05/13/224427)
- [Docker + Alpine3.5 + Apache2.4 + Python3.6で、SSIを使ってみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/05/16/070754)
- [Docker + Alpine3.5 + Apache2.4 + Python3.6で、CGIのリダイレクトを使ってみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/05/21/080250)
- [Docker + Alpine3.5 + Apache2.4 + Python3.6で、CGIのCookieを使ってみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/05/22/061030)
- [Docker + Alpine3.5 + Apache2.4 + Python2.7で、mod_pythonをソースコードからインストールしてみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/06/01/223519)
- [Docker + Alpine3.5 + Apache2.4 + Python3.xで、mod_pythonをソースコードからインストールしてみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/06/10/104538)