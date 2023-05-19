#!/bin/bash

if [ "$#" -lt 1 ]; then
  echo "./preprocess_AGENDA.sh <dataset_folder>"
  exit 2
fi

processed_data_folder='processed'
mkdir -p ${processed_data_folder}

python preprocess/generate_input_agenda.py ${1} ${processed_data_folder}



