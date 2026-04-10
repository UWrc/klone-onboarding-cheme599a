#!/bin/bash

#SBATCH --job-name=klone_demo
#SBATCH --partition=ckpt-all
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus=2080ti:1
#SBATCH --mem=1G
#SBATCH --time=00:10:00
#SBATCH --output=%x-%j.out

module load conda
conda activate base

python klone_demo.py