# Facebook Prophet Docker

This repo contains a Docker container for running [Prophet](https://facebook.github.io/prophet/).

Build your image:

	docker build -t fbprophet-notebook:latest .

Run the container:

	docker run  -dit --rm --name adv_dsi_lab_2 -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work fbprophet-notebook:latest

Print logs of image:

    docker logs --tail 50 adv_dsi_lab_2

To stop the container: 

	docker stop adv_dsi_lab_2


