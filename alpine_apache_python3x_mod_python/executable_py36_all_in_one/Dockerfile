# ビルド
# docker image build -t thinkami:python35_httpd24_mod_python_allinone .
# docker container run -p 8081:80 --name mod_python_allinone -v `pwd`/htdocs/:/usr/local/apache2/htdocs thinkami:python35_httpd24_mod_python_allinone

FROM alpine:3.5

#--------------------------------------------------
# Apache2.4
# このDockerfileの元となったものは、公式のもの
# https://github.com/docker-library/httpd/blob/656b3859734d70b47386fd8bac58d5f719df596b/2.4/alpine/Dockerfile
# ディレクトリにある`httpd-foreground`は `chmod 755httpd-foreground` しておく
#--------------------------------------------------
# ensure www-data user exists
RUN set -x \
  && addgroup -g 82 -S www-data \
  && adduser -u 82 -D -S -G www-data www-data
# 82 is the standard uid/gid for "www-data" in Alpine
# http://git.alpinelinux.org/cgit/aports/tree/main/apache2/apache2.pre-install?h=v3.3.2
# http://git.alpinelinux.org/cgit/aports/tree/main/lighttpd/lighttpd.pre-install?h=v3.3.2
# http://git.alpinelinux.org/cgit/aports/tree/main/nginx-initscripts/nginx-initscripts.pre-install?h=v3.3.2

ENV HTTPD_PREFIX /usr/local/apache2
ENV PATH $HTTPD_PREFIX/bin:$PATH
RUN mkdir -p "$HTTPD_PREFIX" \
  && chown www-data:www-data "$HTTPD_PREFIX"
WORKDIR $HTTPD_PREFIX

ENV HTTPD_VERSION 2.4.25
ENV HTTPD_SHA1 bd6d138c31c109297da2346c6e7b93b9283993d2

# https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394
ENV HTTPD_BZ2_URL https://www.apache.org/dyn/closer.cgi?action=download&filename=httpd/httpd-$HTTPD_VERSION.tar.bz2
# not all the mirrors actually carry the .asc files :'(
ENV HTTPD_ASC_URL https://www.apache.org/dist/httpd/httpd-$HTTPD_VERSION.tar.bz2.asc

# see https://httpd.apache.org/docs/2.4/install.html#requirements
RUN set -x \
  && runDeps=' \
    apr-dev \
    apr-util-dev \
    perl \
  ' \
  && apk add --no-cache --virtual .build-deps \
    $runDeps \
    ca-certificates \
    coreutils \
    dpkg-dev dpkg \
    gcc \
    gnupg \
    libc-dev \
    # mod_session_crypto
    libressl \
    libressl-dev \
    # mod_proxy_html mod_xml2enc
    libxml2-dev \
    # mod_lua
    lua-dev \
    make \
    # mod_http2
    nghttp2-dev \
    pcre-dev \
    tar \
    # mod_deflate
    zlib-dev \
  \
  && wget -O httpd.tar.bz2 "$HTTPD_BZ2_URL" \
  && echo "$HTTPD_SHA1 *httpd.tar.bz2" | sha1sum -c - \
# see https://httpd.apache.org/download.cgi#verify
  && wget -O httpd.tar.bz2.asc "$HTTPD_ASC_URL" \
  && export GNUPGHOME="$(mktemp -d)" \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys A93D62ECC3C8EA12DB220EC934EA76E6791485A8 \
  && gpg --batch --verify httpd.tar.bz2.asc httpd.tar.bz2 \
  && rm -r "$GNUPGHOME" httpd.tar.bz2.asc \
  \
  && mkdir -p src \
  && tar -xf httpd.tar.bz2 -C src --strip-components=1 \
  && rm httpd.tar.bz2 \
  && cd src \
  \
  && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
  && ./configure \
    --build="$gnuArch" \
    --prefix="$HTTPD_PREFIX" \
    --enable-mods-shared=reallyall \
    # デフォルトはpreforkにする
    --with-mpm=prefork \
    # ただし、他のMPMもビルドする：この指定がない場合、MPMのmoduleがないので切り替えられない
    # http://tt4cs.blogspot.jp/2013/01/how-to-enable-dso-for-apache-2.4.html
    --enable-mpms-shared=all \
  && make -j "$(nproc)" \
  && make install \
  \
  && cd .. \
  && rm -r src man manual \
  \
  && sed -ri \
    -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
    -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
    "$HTTPD_PREFIX/conf/httpd.conf" \
  \
  && runDeps="$runDeps $( \
    scanelf --needed --nobanner --recursive /usr/local \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
  )" \
  && apk add --virtual .httpd-rundeps $runDeps \
  && apk del .build-deps

# ローカルでchmod 755しておく
COPY httpd-foreground /usr/local/bin/

EXPOSE 80
CMD ["httpd-foreground"]


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