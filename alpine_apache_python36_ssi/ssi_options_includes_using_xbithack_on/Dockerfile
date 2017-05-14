FROM httpd:2.4.25-alpine

# 以下のDockerfileを、httpdをベースに、apkのEdgeから3.6を持ってくるように修正し、python3をインストール
# https://github.com/frol/docker-alpine-python3
# http://qiita.com/ma2shita/items/4422777ff3ab8cf27171
RUN apk --update --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ add python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

# ローカルのhttpd.confをコピー
COPY httpd.conf /usr/local/apache2/conf/