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


# Copy files out of container
```
ID=$(docker create my-lambda /bin/true)	
docker cp $ID:/lambda .			
```