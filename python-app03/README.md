# Docker-Kafka-Python

Small docker image with python kafka app noroot user executing python app


# Requirements

- Python (http://python.org)
- kafka-python (pip install kafka-python)
- Docker (http://docker.com)


# Create image
docker build -t python-app03 .

# Run image
docker run python-app03