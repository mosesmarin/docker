# Python env for aws lambda 

Used to develop code for aws lambda and api gateway
In this example lambda code is created



# Requirements

- Python (http://python.org)
- Docker (http://docker.com)
- qrcode
- pillow

# Create image
```
docker build -t python-app07 .
docker build -t lambda-code .

```
# Run image
```
docker run -it python-app07 /bin/bash
docker run -it lambda-code /bin/bash
```
# Kubectl
```
kubectl create deployment python-app07 --image=m0ses1/python-app:07
```


# Copy files out of container
```
docker container ls
docker cp b2a93a8f8c52:/lambda.zip .
```