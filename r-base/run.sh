#!/bin/bash

DATA_DIR=../data
DATA_FILE=deliveryData_2.csv
SCRIPT=sample.r
CMD=./r-3.5.0/Rscript

echo "run.sh >> start"

echo "...SCRIPT_DIR..."
ls ./

echo "...DATA_DIR..."
ls $DATA_DIR

$CMD $SCRIPT $DATA_DIR/$DATA_FILE
