
## Steps to connect node application with mongodb running in docker container

 - Create a docker network for container
 ```
 docker network create mongo-net
 ```
 - Run "mongo" container for database
  ```
 docker run -d \                                                             
-p27017:27017 \
--name mongo \
--network mongo-net \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=admin \
mongo
 ```
 - Run "mongo-express" container for interface
 ```
docker run -d \                                                            
-p8081:8081 \
--name mongo-express \
--network mongo-net \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=admin -e ME_CONFIG_MONGODB_URL="mongodb://admin:admin@mongo:27017" \
mongo-express
 ```
 - Run Node Application with connection to mongodb
