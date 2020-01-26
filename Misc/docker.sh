#Install docker : 
Follow this commands : https://docs.docker.com/install/linux/docker-ce/ubuntu/

#Get the existing container list:
docker ps

#Start a container:
docker run --name my_docker image_name # for example : docker run --name janusgraph-default janusgraph/janusgraph:latest

#getting bash shell to a running container:
docker exec -it <container name> /bin/bash

#Stop container : 
docker stop [OPTIONS] CONTAINER [CONTAINER...]

#Remove a container :
sudo docker container rm CONTAINER_ID

#Find info about the images
sudo docker images

#Container configurations
sudo docker inspect CONTAINER

#Container stats
sudo docker stat CONTAINER