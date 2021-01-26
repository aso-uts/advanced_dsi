FROM jupyter/scipy-notebook:0ce64578df46

RUN conda install yellowbrick

RUN pip install mlflow==1.13

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

RUN echo "export PYTHONPATH=/home/jovyan/work" >> ~/.bashrc

WORKDIR /home/jovyan/work
