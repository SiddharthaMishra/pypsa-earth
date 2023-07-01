FROM continuumio/miniconda3:22.11.1
RUN apt clean && apt update
RUN apt install -y git wget curl build-essential default-jre

RUN conda install -c conda-forge mamba
COPY ./envs/pypsa-earth.yaml .
RUN mamba env create --file pypsa-earth.yaml -n pypsa-earth
WORKDIR /pypsa-earth
RUN conda remove mamba && apt remove -y git gcc build-essential
COPY . .
CMD ["./run.sh"]

