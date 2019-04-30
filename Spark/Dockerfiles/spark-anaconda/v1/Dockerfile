FROM java:8-jdk-alpine

#Instalar dependencias de build.

WORKDIR /tmp

RUN apk add --no-cache build-base linux-headers wget ca-certificates bash 

#Instalar Python3 e Pip3
RUN apk add --no-cache python3 python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

#Instalar Scala
ENV SCALA_VERSION=2.12.8 \
    SCALA_HOME=/usr/share/scala

RUN wget "https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" \
 && tar xzf "scala-${SCALA_VERSION}.tgz" \
 && mkdir "${SCALA_HOME}" \
 && mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib" "${SCALA_HOME}" \
 && ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" \
 && rm -rf "/tmp/"*

#Instalar SPARK
ENV SPARK_HOME=/usr/spark-2.4.1-bin-hadoop2.6 \
    HADOOP_HOME=/usr/hadoop-2.6.3

ADD http://archive.apache.org/dist/hadoop/common/hadoop-2.6.3/hadoop-2.6.3.tar.gz hadoop-2.6.3.tar.gz
ADD https://archive.apache.org/dist/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.6.tgz spark-2.4.1-bin-hadoop2.6.tgz

RUN tar -C /usr -xzf hadoop-2.6.3.tar.gz && \
    tar -C /usr -xzf spark-2.4.1-bin-hadoop2.6.tgz && \
    rm -rf $HADOOP_HOME/share/doc && \
    rm -rf $SPARK_HOME/examples && \
    rm -rf $SPARK_HOME/ec2 && \
    rm -rf /tmp/*

#Instalar pacotes Python
RUN pip3 install jupyter
RUN pip3 install py4j
RUN pip3 install findspark
RUN pip3 install pyspark

RUN mkdir -p /opt/notebooks 

VOLUME /opt/notebooks 

EXPOSE 8888

ENTRYPOINT [ "jupyter" ] 
CMD ["notebook", "--notebook-dir=/opt/notebooks", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root" ]