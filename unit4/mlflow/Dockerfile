FROM python:3.7.0

RUN mkdir /mlflow/

RUN pip install mlflow==1.13

EXPOSE 5000

CMD mlflow server \
    --file-store /mlflow \
    --host 0.0.0.0
