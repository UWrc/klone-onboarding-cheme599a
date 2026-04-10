# Scheduling Jobs on Hyak Klone

When you first log in to Klone, you land on a shared login node (`klone-login01`). Login nodes are for light activity like transferring data, setting up environments, and preparing job scripts.

🛑 **Do not run compute-heavy work here**. All compute work must be run through the job scheduler.

Klone uses Slurm, a workload manager that allocates compute resources on the cluster. Slurm coordinates who gets CPUs and GPUs, when jobs run, and where they run.

## Understanding Job Types

There are two main ways to run work on Klone:

| Job Type            | Command  | Best For                     | Runs On                                         |
| ------------------- | -------- | ---------------------------- | ----------------------------------------------- |
| **Interactive Job** | `salloc` | Exploratory or hands-on work | A compute node you connect to directly          |
| **Batch Job**       | `sbatch` | Long or unattended jobs      | Runs automatically when resources are available |


Klone jobs are submitted under a combination of **account** and **partition**, which defines resource limits like CPU/GPU count and memory based on hardware holdings of the account.

> 💡 **TIPS**: Use `hyakalloc` to find available compute resources.

## Interactive Jobs with `salloc`

Interactive jobs give you a live shell on a compute node — great for testing or exploring.

Run the following to start an interactive session using 1 CPU:

```bash
salloc --partition=ckpt-all --cpus-per-task=1 --mem=10G --time=1:00:00
```

When the job starts, you’ll see the following:

```bash
salloc: Granted job allocation 34515117
salloc: Waiting for resource configuration
salloc: Nodes n3319 are ready for job
```

> 📝 **NOTE:** The hostname changed from `klone-login01` to a compute nodelist (e.g., `n3319`). You are now on a compute node. 

> 💡 **TIPS:** If you have trouble with a job, saving the jobID (e.g. above, 34515117) allows us to investigate what was going on when your job failed.

Now you can run code and scripts interactively on a compute node.

To end the session, type:

```bash
exit
```

> 💡 **TIPS**: To request an interactive session on a GPU:
>
> ```bash
> salloc --partition=ckpt-all --gpus-per-node=a40:1 --mem=10G --time=1:00:00 
> ```
> Confirming the GPU is Active:
>
> ```bash
> nvidia-smi
> ```

## Batch Jobs with `sbatch`

Batch jobs run automatically without supervision. The following is an example of a script that can be used to schedule a job on Klone:

```bash
cat 
```
job.slurm
```bash
#!/bin/bash

#SBATCH --job-name=myjob
#SBATCH --partition=ckpt-all
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=1G
#SBATCH --time=00:10:00
#SBATCH --output=slurm-%j.out
#SBATCH --open-mode=append

hostname
```

For more details on the `#SBATCH` directives, refer to [<ins>sbatch manual</ins>](https://slurm.schedmd.com/sbatch.html).

You would submit the job with:

```bash
sbatch job.slurm
```

Slurm will return a job ID and queue it for execution.

To cancel a pending or running job, run:

```bash
# replace <job_id> with the real jobID returned by Slurm.
scancel <job_id>
```

## Monitoring Jobs

Check your running and pending jobs:

```bash
squeue -u $USER
```

This command lists all your active or queued jobs. You’ll see columns such as:

| Column | Meaning |
| --- | --- |
| **JOBID** | A unique number assigned to your job. Use this to reference it in other commands. |
| **PARTITION** | The resource pool or QOS (e.g., `cpu-g2`, `gpu-rtx6k`, `ckpt-all`) |
| **NAME** | The job name specified with `--job-name` |
| **ST** | Job status: <br> `PD` (Pending), `R` (Running), `CG` (Completing), `CD` (Completed) |
| **TIME** | Runtime duration |
| **NODELIST(REASON)** | Node(s) assigned to the job or reason for pending (e.g., “Resources” or “Priority”) |

For more details or to customize the output format of squeue, refer to [<ins>squeue manual</ins>](https://slurm.schedmd.com/squeue.html).

Use `sinfo -r` to check cluster-wide node availability.

Once it’s finished, view the output:

```bash
# replace <jobID> above with the jobID
cat slurm_<jobID>.out
```