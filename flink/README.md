# Docker-Alpine-OpenJDK-Flink

Base linux with Flink


# Requirements

- Docker (http://docker.com)

# Start cluster and look at Dispatcher's web front end
```
cd flink-1.9.1
./bin/start-cluster.sh
http://localhost:8081/
```

# Create image
```
docker build -t flink01 .
```
# Run image
```
docker run -it flink01 /bin/sh
docker run -it --expose 8081 -p 8081:8081 flink01 /bin/sh 
```
