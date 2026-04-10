<!-- omit in toc -->
# Hands-on Exercise: Running a Python Script on Klone

This hands-on exercise will guide you through the essential steps for using Klone:

You’ll create a working directory, start an interactive job, load modules, run Python code, submit a batch job.

> 🎯 **GOAL:** Learn how to build and run a simple workflow on Klone using terminal command line interface.

**Overview**

- [0. Create Your Working Directory](#0-create-your-working-directory)
- [1. Start an Interactive Job](#1-start-an-interactive-job)
- [2. Load Conda Module](#2-load-conda-module)
- [3. Run a Simple Python Script](#3-run-a-simple-python-script)
- [4. Submit a Batch Job](#4-submit-a-batch-job)

## 0. Create Your Working Directory

If you have not already completed the preparations steps, please follow the instructions in [<ins>00-prereqs.md</ins>](./00-prereqs.md) and [Filesystem Scrubbed section](./02-filesystem.md#5-scrubbed-storage--our-tutorial-workspace) to set up your Hyak account, log in to Klone, and clone the git repository for this tutorial in a proper location.

Navigate to your working directory for this tutorial:

```bash
cd /gscratch/scrubbed/$USER/klone-onboarding-cheme599a
```

## 1. Start an Interactive Job

> ⚠️ **WARNING:** All compute work must run on compute nodes — **never** on the login node.

Check compute resources available using:

```bash
hyakalloc
```

Request an interactive session with 1 GPU for 30 minutes:

```bash
salloc --partition=ckpt-all --gpus=2080ti:1 --mem=10G --time=00:30:00
```

Once resources are allocated, confirm you're on a compute node:

```bash
hostname
```

You should see the hostname change from `klone-login0*` to something like `g***`.

Check GPU availability:

```bash
nvidia-smi
```

If you see GPU details (e.g., NVIDIA H200 with driver and CUDA versions), you're ready to compute.

## 2. Load Conda Module

> ⚠️ **WARNING:** To install GPU-aware packages (e.g., PyTorch, TensorFlow), always request a GPU node for the installation.

List available modules and locate Conda:

```bash
module avail
module spider conda
```

Load the system Conda module:

```bash
module load conda
```

Activate the base environment:

```bash
conda activate base
```

Verify Python is ready in your environment:

```bash
which python
python --version
```

You'll see the full path such as `/mmfs1/sw/miniforge3/25.9.1-0/bin/python`, and `python --version` returns "Python 3.12.12".

## 3. Run a Simple Python Script

A simple demo script `klone_demo.py` is provided in the training repository. Run it as follows:

```bash
python klone_demo.py 2>/dev/null
```

Here, `2>/dev/null` redirect standard error to `/dev/null` when running the script.

You’ll see console output like:

```plain text
▶️ Starting Klone demo job...
Hostname: z****
User: user
Python version: 3.12.12

Checking GPU availability with nvidia-smi...
GPU detected:
  GPU 0: NVIDIA GeForce RTX 2080 Ti, 11264 MiB, 1 MiB

✅ Completed successfully.
```

This verifies that your GPU is detectable.

## 4. Submit a Batch Job

Now, let's run the same task as a batch job using Slurm so it can run unsupervised.

Deactivate your environment and exit your interactive shell:

```bash
conda deactivate
exit
```

A template job script is included in the training repository. Review it before submitting the job:

```bash
cat klone_demo.slurm
```

> 💡 **TIP:** `#SBATCH --output=%x-%j.out` redirect both standard output (`stdout`) and standard error (`stderr`)to the file specified `%x_%j.out`, where `%x` and `%j` expand to the job name specified and job ID allocated.

Submit a batch job:

```bash
sbatch klone_demo.slurm
```

Slurm will return a job ID.

Monitor your pending and running jobs:

```bash
squeue -u $USER
```

When the job finishes, view results:

```bash
cat klone_demo-*.out
```