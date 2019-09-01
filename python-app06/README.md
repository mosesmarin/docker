# Python env for aws lambda 

Used to develop code for aws lambda and api gateway



# Requirements

- Python (http://python.org)
- Docker (http://docker.com)
- qrcode
- pillow

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
