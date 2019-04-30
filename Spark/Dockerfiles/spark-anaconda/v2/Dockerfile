FROM alpine:3.9

# Install glibc and useful packages
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && apk --update add \
    curl \
    ca-certificates \
    libstdc++ \
    glib \
    tini@testing \
    && curl "https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub" -o /etc/apk/keys/sgerrand.rsa.pub \
    && curl -L "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk" -o glibc.apk \
    && apk add glibc.apk \
    && curl -L "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-bin-2.29-r0.apk" -o glibc-bin.apk \
    && apk add glibc-bin.apk \
    && curl -L "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-i18n-2.29-r0.apk" -o glibc-i18n.apk \
    && apk add --allow-untrusted glibc-i18n.apk \
    && /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \
    && /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib \
    && rm -rf glibc*apk /var/cache/apk/*

ENV ANACONDA_VERSION 2019.03
ENV ANACONDA_MD5 43caea3d726779843f130a7fb2d380a2

# Create non-root user, install dependencies, install Anaconda
RUN addgroup -S anaconda && \
    adduser -D -u 10151 anaconda -G anaconda && \
    curl https://repo.continuum.io/archive/Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh -o anaconda.sh && \
    echo "${ANACONDA_MD5}  anaconda.sh" > anaconda.md5 && \
    if [ $(md5sum -c anaconda.md5 | awk '{print $2}') != "OK" ] ; then exit 1; fi && \
    mkdir -p /opt && \
    sh ./anaconda.sh -b -p /opt/conda && \
    rm anaconda.sh anaconda.md5 && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    chown -R anaconda /opt && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/anaconda/.profile && \
    echo "conda activate base" >> /home/anaconda/.profile

USER  10151
ENV PATH "/bin:/sbin:/usr/bin"

CMD [ "sh", "--login", "-i" ]