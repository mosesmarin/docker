------------------------------------------------------------------------------
# Container that has python code to read from kafka cluster


## Setup java and java consumer producer
sudo yum install java-1.8.0
wget ftp://apache.cs.utah.edu/apache.org/kafka/2.2.0/kafka_2.12-2.2.0.tgz
tar -xzf kafka_2.12-2.2.0.tgz
cd kafka_2.12-2.2.0/

## Check if MKS cluster is active
aws kafka describe-cluster --region us-east-1 --cluster-arn "arn:aws:kafka:us-east-1:705115062918:cluster/demo-cluster/87730fba-dbdd-4764-8450-26229e600167-2"

## set account keys if needed
aws configure

## Create Topic
bin/kafka-topics.sh --create --zookeeper "172.31.23.57:2181,172.31.2.237:2181,172.31.83.25:2181" --replication-factor 3 --partitions 1 --topic KAFKA-TOPIC

## Find Broker
aws kafka get-bootstrap-brokers --region us-east-1 --cluster-arn arn:aws:kafka:us-east-1:705115062918:cluster/demo-cluster/87730fba-dbdd-4764-8450-26229e600167-2

## Producer and consumer
bin/kafka-console-producer.sh --broker-list "servers:9092" --topic KAFKA-TOPIC
bin/kafka-console-consumer.sh --bootstrap-server "servers:9092" --topic KAFKA-TOPIC --from-beginning

## Setup python consumer and producer
yum -y install python-pip
pip install kafka-python
./python-example.py

---------------------------------------------------


# kubectl commands

## Launch kubernetes shell-demo
kubectl apply -f https://k8s.io/examples/application/shell-demo.yaml
kubectl exec -it shell-demo -- /bin/bash


## push image to docker hub
docker images
--find image id , then tag with repository
docker tag 56e3b6fbe337 m0ses1/python-app:01
docker tag 542b520442f7 m0ses1/python-app:02
docker tag eb5d23876f5d m0ses1/python-app:03
docker tag 6ccddf34c1a1 m0ses1/python-app:04
docker push m0ses1/python-app:01
docker push m0ses1/python-app:02
docker push m0ses1/python-app:03
docker push m0ses1/python-app:04


## Create k8s deployment 
kubectl create deployment python-app01 --image=m0ses1/python-app:01
kubectl create deployment python-app02 --image=m0ses1/python-app:02
kubectl create deployment python-app03 --image=m0ses1/python-app:03
kubectl create deployment python-app04 --image=m0ses1/python-app:04

## log into pod
kubectl exec -it python-app03-5d48d5bfd7-2bc2v -- /bin/sh

kubectl describe pod

## delete deployment (termiantes pod)
kubectl get deployments
kubectl delete deployment python-app01
kubectl delete deployment python-app02
kubectl delete deployment python-app03
kubectl delete deployment python-app04

## delete pod
kubectl get pods
kubectl delete pods python-app02-77cfff7fc7-vhl9s

## More k8s commands
kubectl cluster-info
kubectl get events


--------------------------------------------------
# Docker commands

## delete image
docker rmi python-app01
docker rmi -f python-app01

## check containers 
docker ps
docker kill 
docker system prune

## kill all running containers with 
docker kill $(docker ps -q)

## delete all stopped containers with 
docker rm $(docker ps -a -q)

## delete all images with 
docker rmi $(docker images -q)

## create docker image and container
docker images
docker build -t python-application .
docker run python-application
docker run -it alpine /bin/sh


## Export Image
Run the following command to save Docker image as a tar file.
docker save -o ./python-app04.tar python-app04
docker save python-app04 > python-app04.tar
docker load --input python-app04.tar


--------------------------------------------------
# URLS


## Create docker image
https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9

## Python app example
https://www.tutorialkart.com/docker/docker-image-with-python-application-example/
pip install --target=/home/ec2-user/python-application kafka-python


## kafka requirements for pip install 
https://github.com/OpenBankProject/OBP-Kafka-Python

## Size of image
https://stackoverflow.com/questions/31060871/big-size-of-python-image-in-docker
https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3


## for kubernetes deployment
https://blog.docker.com/2013/07/how-to-use-your-own-registry/
https://www.mirantis.com/blog/introduction-to-yaml-creating-a-kubernetes-deployment/

## docker registry
https://docs.docker.com/registry/
