# Xgboost Docker

This repo contains a Docker container for running [Xgboost](https://xgboost.readthedocs.io/).

Build your image:

	docker build -t myimage .

Run the container:

	docker run -d -p 8888:8888 myimage

To stop the container: 

	docker stop myimage


