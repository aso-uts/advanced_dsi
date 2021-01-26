FROM jupyter/scipy-notebook:0ce64578df46

RUN conda install -y pytorch torchvision

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

RUN echo "export PYTHONPATH=/home/jovyan/work" >> ~/.bashrc

WORKDIR /home/jovyan/work