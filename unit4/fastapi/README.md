# FastAPI Docker

This repo contains a Docker container for running  [FastAPI](https://fastapi.tiangolo.com/).

- Build your FastAPI image:
	`docker build -t myimage .`

- Run the container:
	`docker run -d --name mycontainer -p 80:80 myimage`

- Test the endpoint:
	`http://127.0.0.1:8000/items/5?q=somequery`

- Check the documentation:
	`http://127.0.0.1:8000/docs`


