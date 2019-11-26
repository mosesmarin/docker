# Alpine Linux with OpenJDK JRE
FROM openjdk:8-jre-alpine

RUN apk add bash

COPY . /app
RUN wget http://apache-mirror.8birdsvideo.com/flink/flink-1.9.1/flink-1.9.1-bin-scala_2.12.tgz  && tar xzf flink-1.9.1-bin-scala_2.12.tgz -C /app && rm /*tgz


WORKDIR /app

CMD ["/bin/sh"]


