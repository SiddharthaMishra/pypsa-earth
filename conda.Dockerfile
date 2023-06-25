FROM continuumio/miniconda3:23.3.1-0 AS build
RUN apt update && apt install -y --no-install-recommends  git wget curl build-essential default-jre

RUN conda install -c conda-forge mamba
COPY ./envs/pypsa-container.fixed.yaml .
RUN mamba env create --file pypsa-container.fixed.yaml -n pypsa-earth
WORKDIR /pypsa-earth
RUN conda remove mamba && apt remove -y git gcc build-essential
COPY . .
CMD ["./run.sh"]

