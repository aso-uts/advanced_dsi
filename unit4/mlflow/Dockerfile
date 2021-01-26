FROM python:3.7.0

RUN mkdir /mlstore/ /mlruns/

RUN pip install mlflow[extras]==1.13

EXPOSE 5000

CMD ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "/mlstore", "--default-artifact-root" , "/mlruns"]