FROM centos/python-34-centos7

RUN git clone https://github.com/confluentinc/confluent-kafka-python.git

COPY ./consumer.py /app/
COPY ./consumer-parms.py /app/

COPY ./install-requirements.sh /opt/app-root/src
COPY ./confluence.repo /etc/yum.repos.d/

USER root

RUN yum clean all
RUN yum -y install librdkafka-devel python-devel
RUN sh /opt/app-root/src/install-requirements.sh

RUN useradd -u 10001 10001
RUN chown -R 10001 /app
RUN chgrp -R 10001 /app

WORKDIR /app


USER 10001


CMD ["python3", "consumer.py"]