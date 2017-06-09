# ビルド
# docker image build -t thinkami:python35_httpd24_mod_python_patched .
# docker container run -p 8081:80 --name mod_python_patched -v `pwd`/htdocs/:/usr/local/apache2/htdocs thinkami:python35_httpd24_mod_python_patched

FROM thinkami:httpd24_prefork

#--------------------------------------------------
# mod_pythonのインストール
#--------------------------------------------------
# EdgeのPython3パッケージを持ってくる
RUN apk --update --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ add python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    # mod_pythonで必要なパッケージを追加
    apk add --no-cache --virtual .mod_python_build_libs git && \
    # python3-devもEdgeから持ってくる
    # そうでないと、Python3のバージョンが合わずに、Downgrading python3が発生する
    apk --no-cache --virtual .mod_python_build_libs --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ add python3-dev && \
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
    # gitを使うためにユーザ設定を実施
    git config --global user.email "you@example.com" && \
    git config --global user.name "Your Name" && \
    # 現在のmasterを取得
    git clone https://github.com/grisha/mod_python.git . && \
    # 3.5.xブランチを取得
    git branch 3.5.x origin/3.5.x && \
    # 3.5.xブランチをmasterにマージ
    git merge 3.5.x && \
    # python3用に、masterブランチのうちの一部ファイルを3.5.xブランチの状態へ戻す => OK
    git checkout 2d013b353631feb7ffe29fe9946327a08fe55381 scripts/mod_python.in && \
    git checkout 54d42b1810d5abfffe5b407d8e763402a0d4b2f0 configure.in && \
    git checkout 9d223c39a8f27345d8c046d026468fc0c1ad5d53 configure && \
    git checkout 51f7b0366d66b58b5b82874fe8a2db346f77d7fc src/include/mod_python.h && \
    git checkout 51f7b0366d66b58b5b82874fe8a2db346f77d7fc src/include/mod_python.h.in && \
    git checkout affc26bd69b3f5e67e8233166ff0d40c43fb7302 src/mod_python.c && \
    # ビルド
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