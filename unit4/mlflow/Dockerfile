FROM python:3.7-stretch

RUN pip install mlflow==1.13

RUN mkdir /mlflow/
RUN mkdir /mlflow/mlstore/
RUN mkdir /mlflow/mlruns/

WORKDIR /mlflow

CMD ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "/mlflow/mlstore", "--default-artifact-root" , "/mlflow/mlruns"]