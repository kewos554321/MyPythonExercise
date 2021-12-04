#!/bin/bash
#PBS -l nodes=cn1
module load app/anaconda3/2019.10/x86_64
cd data
python test.py 19-30
