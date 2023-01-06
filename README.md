# Mobelux Challenge

## Notes

This application is for Linux or MacOS. Windows is not supported.

## Setup
- install docker [DOCKER](https://docs.docker.com/get-docker/)
- for linux run in terminal of base directory of repository `sudo docker-compose up`
- for MacOS run in terminal of base directory of repository `docker-compose up`

### Creating super user
- run in terminal of base directory of repository `sudo docker ps`
  -  copy the container_id for the be contianer not the database container
  - run command without brackets just paste in container id after -it `sudo docker exec -it {paste_container_id} bash`
  - once in the container run command `pipenv shell`
  - once on pipenv shell run command `cd application`
  - once in the application directory run command `python manage.py createsuperuser` and follow prompt to create user.
  - go to your browser and go to address localhost:8000/admin and login with superuser credentials
  - create user via django admin interface.

### Web app endpoints
1. Http://localhost:8000 - home page and create album interface
2. http://localhost:8000/accounts/logout/ - log of session
3. http://localhost:8000/albums/ - list of albums for signes in user
4. http://localhost:8000/albums/<pk>/ - list of images of album_id(pk) and image uplaod for album_id(pk)

### WEb api endpoints
1. http://localhost:8000/api/albums/ -  Django Rest Framework endpoint for all albums to signed in user
2. http://localhost:8000/api/albums/<pk> -  Django Rest Framework endpoint for all images for album_id(pk in url)