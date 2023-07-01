FROM continuumio/miniconda3:23.3.1-0
RUN apt clean && apt update
RUN apt install -y git wget curl build-essential default-jre

RUN conda install -c conda-forge mamba
COPY ./envs/environment.yaml .
RUN mamba env create --file environment.yaml -n pypsa-earth
WORKDIR /pypsa-earth
RUN conda remove mamba && apt remove -y git gcc build-essential
COPY . .
CMD ["./run.sh"]

