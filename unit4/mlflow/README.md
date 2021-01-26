# MLflow Docker

This repo contains a Docker container for running  [MLflow](https://mlflow.org/).

To build the image: 

    docker build -t mlflow .

To run the container: 

	docker run -p 5000:5000 mlflow
	
To stop the container: 

	docker stop myimage
