# Docker_Apache-sample

# Tested environment

- Mac OS X 10.11.6
- Docker for Mac 17.03.0-ce-mac2

　  
# Samples

- alpine_apache_python36_cgi/
  - run Apache2.4.25 + Python3.6.0 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.4
    - base Dockerfile: httpd:2.4.25-alpine, python:3.6.0-alpine
- alpine_apache_python36_cgi_form
  - run Apache2.4.25 + Python3.6.1 + Python CGI Script on Docker
  - Dockerfile environment
    - Alpine3.5
    - base Dockerfile: httpd:2.4.25-alpine, frolvlad/alpine-python3

　  
# Related Blog (Written in Japanese)

- [Dockerで、Alpine3.4 + Apache2.4.25 + Python3.6.0の環境を作って、CGIを動かしてみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/03/15/062314)
- [Dockerで、Alpine3.5 + Apache2.4 + Python3.6の環境を作って、フォームのデータをCGIで受け取ってみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/05/10/214559)