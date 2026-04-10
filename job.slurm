#!/bin/bash
#SBATCH --job-name=myjob
#SBATCH --partition=ckpt-all
#SBATCH --cpus-per-task=1
#SBATCH --mem=10G
#SBATCH --time=01:00:00
#SBATCH --output=slurm-%j.out

hostname