FROM jarzamendia/alpine-scala2.12.8-spark-base-ed:3.9

COPY worker.sh /

ENV SPARK_WORKER_WEBUI_PORT 8081
ENV SPARK_WORKER_LOG /spark/logs
ENV SPARK_MASTER "spark://spark-master:7077"

EXPOSE 8081

CMD ["/bin/bash", "/worker.sh"]

ARG BUILD_DATE

# Labels.
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="alpine-base-ed"
LABEL org.label-schema.description="Imagem base para Engenharia de Dados"
LABEL org.label-schema.url="https://alpinelinux.org/"
LABEL org.label-schema.vendor="Alpine"
LABEL org.label-schema.version="1"