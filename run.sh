#!/usr/bin/env bash

if [ -z $SUBCOMMAND]; then
    echo "Please set SUBCOMMAND"
    exit(1)
fi

conda activate pypsa-earth 
python container-helpers/download-configs.py
if [  $SUBCOMMAND = "prepare" ]; then
    snakemake -j $(nproc --all) upload_all_prepared_networks
elif [ $SUBCOMMAND = "run" ]; then
    python container-helpers/download-network.py
    snakemake -j $(nproc --all) upload_solved_network "results/$PREPARED_NETWORK_OPTS.uploaded.done"
