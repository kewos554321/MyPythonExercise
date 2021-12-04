#!/bin/bash
#PBS -l nodes=cn1
cd data
python test.py 121-129
module load app/anaconda3/2019.10/x86_64
