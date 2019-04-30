FROM jarzamendia/alpine-java8jdk-ed:3.9

#Install Python3, and change the path to Python.
RUN apk add --no-cache python3 python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

ARG BUILD_DATE

# Labels.
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="alpine-python-ed"
LABEL org.label-schema.description="Imagem com Python para Engenharia de Dados"
LABEL org.label-schema.url="https://alpinelinux.org/"
LABEL org.label-schema.vendor="Alpine"
LABEL org.label-schema.version="1"