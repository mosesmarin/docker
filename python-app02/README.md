# Docker-Kafka-Python

Small docker image with python kafka app noroot user


# Requirements

- Python (http://python.org)
- kafka-python (pip install kafka-python)
- Docker (http://docker.com)


# Create image
docker build -t python-app02 .

# Run image
docker run -it python-app02 /bin/sh