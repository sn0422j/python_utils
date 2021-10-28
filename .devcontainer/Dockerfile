FROM continuumio/miniconda3:4.10.3

COPY .devcontainer/environment.yml /tmp/conda-tmp/environment.yml
RUN /opt/conda/bin/conda env create -f /tmp/conda-tmp/environment.yml
