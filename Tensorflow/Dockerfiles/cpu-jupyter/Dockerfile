FROM jarzamendia/alpine-base-ed:3.9

COPY bashrc /etc/bash.bashrc
RUN python --version

RUN chmod a+rwx /etc/bash.bashrc && \
    apk add --no-cache --allow-untrusted --repository http://dl-3.alpinelinux.org/alpine/edge/testing hdf5 hdf5-dev && \
    apk add --no-cache bash freetype-dev musl-dev build-base && \
    python -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.13.1-cp36-cp36m-linux_x86_64.whl && \
    pip install cython && \
    pip install jupyter matplotlib && \
    pip install jupyter_http_over_ws && \
    jupyter serverextension enable --py jupyter_http_over_ws && \
    python -m ipykernel.kernelspec

WORKDIR /tf

EXPOSE 8888

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root"]

ARG BUILD_DATE

# Labels.
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="tensorflow-alpine-cpu-jupyter"
LABEL org.label-schema.description="Imagem com o Tensorflow e jupyter."
LABEL org.label-schema.url="https://www.tensorflow.org"
LABEL org.label-schema.vendor="Tensorflow"
LABEL org.label-schema.version="1"