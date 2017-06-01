#--------------------------------------------------
# Apache2.4のインストール：公式のDockerfileを流用
#--------------------------------------------------
FROM alpine:3.5

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
RUN apk --update --no-cache add python && \
    # mod_pythonで必要なパッケージを追加
    apk add --no-cache --virtual .mod_python_build_libs git && \
    apk add --no-cache --virtual .mod_python_build_libs python-dev && \
    # Apacheはソースコードからインストールしているので、「apache2-dev」は無くても良い
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
    git clone https://github.com/grisha/mod_python.git . && \
    ./configure --with-apxs=/usr/local/apache2/bin/apxs --with-python=/usr/bin/python --with-flex=/usr/bin/flex && \
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