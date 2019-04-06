# Docker-Confluent_Kafka-Python

Centos python docker image with noroot user executing python app



# Requirements

- Python (http://python.org)
- kafka-python (`pip install --target=. kafka-python`)
- Docker (http://docker.com)


# Create image
```
docker build -t python-app05 .
```
# Run image
```
docker run -it python-app05 /bin/sh
```
# Kubectl
```
kubectl create deployment python-app05 --image=m0ses1/python-app:05
```
