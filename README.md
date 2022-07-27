Endpoints:

1)http://127.0.0.1:8000/api/v1/menu/?restaurant={restaurant.id} - get menu by restaurant id

2)http://127.0.0.1:8000/api/v1/make_vote/ - cast your vote

3)http://127.0.0.1:8000/api/v1/add_restaurant/ - add restaurant

4)http://127.0.0.1:8000/api/v1/get_vote/ get total votes
Auth:
5)http://127.0.0.1:8000/api/v1/register/ - register employee

6)http://127.0.0.1:8000/api/v1/login/ - login

7)http://127.0.0.1:8000/api/v1/token/refresh/ - refresh JWT token


Docker:
mkdir PROJECT && cd PROJECT
git init
git clone https://github.com/Nonzeq/Inforce_TZ.git
cd core
docker-compose build
docker-compose up -d


docker stop $(docker ps -a -q) : for stop all containers
docker rm $(docker ps -a -f status=exited -q) : for delete all containers with status exist
docker system prune -a : for delete all images
