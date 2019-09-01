# Docker-Confluent_Kafka-Python

Centos python docker image with noroot user executing python app



# Requirements

- Python (http://python.org)
- kafka-python (`pip install --target=. kafka-python`)
- Docker (http://docker.com)


# Create image
```
docker build -t python-app06 .
```
# Run image
```
docker run -it python-app06 /bin/bash
```
# Kubectl
```
kubectl create deployment python-app06 --image=m0ses1/python-app:05
```


# Copy files out of container
docker container ls
docker cp b2a93a8f8c52:/lambda/image.jpg .
