# ビルド
# docker image build -t thinkami:python35_httpd24_mod_python_3_5_x .
# docker container run -p 8081:80 --name mod_python_35x -v `pwd`/htdocs/:/usr/local/apache2/htdocs thinkami:python35_httpd24_mod_python_3_5_x

FROM thinkami:httpd24_prefork

#--------------------------------------------------
# mod_pythonのインストール
#--------------------------------------------------
# パッケージの最新版を持ってくる
RUN apk --update --no-cache add python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    # mod_pythonで必要なパッケージを追加
    apk add --no-cache --virtual .mod_python_build_libs git && \
    apk add --no-cache --virtual .mod_python_build_libs python3-dev && \
    apk add --no-cache --virtual .mod_python_build_libs apache2-dev && \
    apk add --no-cache --virtual .mod_python_build_libs flex && \
    # ./configureで必要
    apk add --no-cache --virtual .mod_python_build_libs build-base && \
    # sudo make installで必要
    apk add --no-cache --virtual .mod_python_build_libs sudo && \
    # GitHubからソースコードを持ってきてインストール
    cd /tmp && \
    mkdir mod_python && \
    cd mod_python && \
    git clone -b 3.5.x https://github.com/grisha/mod_python.git . && \
    ./configure --with-apxs=/usr/local/apache2/bin/apxs --with-python=/usr/bin/python3 --with-flex=/usr/bin/flex && \
    make && \
    sudo make install && \
    # 不要なパッケージやソースコードを一括削除
    apk del .mod_python_build_libs && \
    rm -r /tmp/mod_python


#--------------------------------------------------
# Apacheの設定
#--------------------------------------------------
# ローカルのhttpd.confをコピー
COPY httpd.conf /usr/local/apache2/conf/