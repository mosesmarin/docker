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

# Start additional terminal in existing container
```
docker exec -it <containerID> /bin/sh
```

# Open stream to socket with nc -l -p (throws error without -p) before submitting flink job
```
nc -l -p 9000
```

# Useful Urls
```
https://training.ververica.com/devEnvSetup.html
https://ci.apache.org/projects/flink/flink-docs-release-1.9/getting-started/tutorials/local_setup.html
```

