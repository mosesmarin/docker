# Docker-Python

Small docker image with python noroot user


# Requirements

- Python (http://python.org)
- Docker (http://docker.com)


# Create image
docker build -t python-app01 .

# Run image
docker run -it python-app01 /bin/sh