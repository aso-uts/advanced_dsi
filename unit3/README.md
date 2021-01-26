# Xgboost Docker

This repo contains a Docker container for running [Xgboost](https://xgboost.readthedocs.io/).

Build your image:

	docker build -t xgboost-notebook:latest .

Run the container:

	docker run  -dit --rm --name adv_dsi_lab_3 -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work xgboost-notebook:latest

Print logs of image:

    docker logs --tail 50 adv_dsi_lab_3

To stop the container: 

	docker stop adv_dsi_lab_3


