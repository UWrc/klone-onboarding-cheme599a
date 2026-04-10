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


Klone jobs are submitted under a combination of **account** and **partition**, which defines limits like CPU/GPU count and memory.

## Interactive Jobs with `salloc`

Interactive jobs give you a live shell on a compute node — great for testing or exploring.

Run the following to start an interactive session using 1 GPU:

```bash
salloc --partition=ckpt-all --time=01:00:00
```

When the job starts, you’ll see the following:

```bash
salloc: Granted job allocation 34515117
salloc: Waiting for resource configuration
salloc: Nodes n3319 are ready for job
```

> 📝 **NOTE:** The hostname changed from `klone-login01` to a compute nodelist (e.g., `n3319`). You are now on a compute node. 

> 💡 **TIPS:** If you have trouble with a job, saving and sharing the jobID (e.g. above, 34515117) allows us to investigate what was going on when your job failed. 

To end the session, type:

```bash
exit
```

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
#SBATCH --cpus-per-task=1
#SBATCH --mem=10G
#SBATCH --time=01:00:00
#SBATCH --output=slurm-%j.out

hostname
```

You would submit the job with:

```bash
sbatch job.slurm
```

Slurm will return a job ID and queue it for execution.

## Monitoring Jobs

Check your running and pending jobs:

```bash
squeue -u $USER
```

This command lists all your active or queued jobs. You’ll see columns such as:

| Column | Meaning |
| --- | --- |
| **JOBID** | A unique number assigned to your job. Use this to reference it in other commands. |
| **PARTITION** | The resource pool or QOS (e.g., `normal`, `interactive`). |
| **NAME** | The job name you set in your script (`--job-name`). |
| **ST** | The job’s status — common values include: <br> `PD` (Pending), `R` (Running), `CG` (Completing), `CD` (Completed). |
| **TIME** | How long the job has been running. |
| **NODELIST(REASON)** | The node(s) your job is on, or if pending, the reason it’s waiting (like “Resources” or “Priority”). |

Watch your queue update every 10 seconds:

```bash
watch -n 10 squeue -u $USER
```

Use `sinfo -r` to view cluster status and available nodes.

Once it’s finished, view the output:

```bash
cat slurm_<jobID>.out
# replace <jobID> above with the jobID
```