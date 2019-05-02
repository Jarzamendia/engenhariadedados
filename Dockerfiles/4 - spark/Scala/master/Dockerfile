FROM jarzamendia/alpine-scala2.12.8-spark-base-ed:3.9

COPY master.sh /

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs

EXPOSE 8080 7077 6066

CMD ["/bin/bash", "/master.sh"]

ARG BUILD_DATE

# Labels.
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="alpine-base-ed"
LABEL org.label-schema.description="Imagem base para Engenharia de Dados"
LABEL org.label-schema.url="https://alpinelinux.org/"
LABEL org.label-schema.vendor="Alpine"
LABEL org.label-schema.version="1"