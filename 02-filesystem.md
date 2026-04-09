# Navigating the Filesystem & Understanding Storage

Working effectively on Hyak depends on two core ideas:
1. **Knowing where you are** in the filesystem
2. **Knowing which storage space you are using**

Both of these are controlled through the Linux command line interface (CLI).

## Klone Storage Overview

On Klone, your primary storage locations live under `/mmfs1/`, which is a shared, high-performance filesystem accessible from all login and compute nodes.

So whenever you see a path like:

```bash
/mmfs1/home/UWnetID
```
that means you're accessing your home directory on the storage system, not a local disk on the login node.

![Diagrammatic representation of the Klone filesystem directory tree. The directory tree shows the root directory at the top which holds all subdirectories. The picture is a truncated view of the filesystem showing the root directory and a few directories within it, including mmfs1 and a few directories within mmfs1/: home/ where the Home directories are, sw/ where we keep software, data/ where common datasets are stored, gscratch/ which is scratch space for active work.](/img/filesystem_klone.jpg 'filesystem')
*Diagram - truncated view of the Klone filesystem.*

As shown above, the Klone filesystem is organized under the root directory `/`. Within it, `/mmfs1/` contains several key subdirectories:

* `home/` — individual user home directories for configuration and small files.
* `sw/` — centrally managed shared applications and tools, and user-contributed softwares under `sw/contrib`
* `data/` — curated public or shared research datasets. We have a process by which groups can nominate datasets for storage under our [**<ins>Data Commons</ins>**](https://hyak.uw.edu/docs/data-commons/requirements). 
* `gscratch/` — scratch space for active work
  * `gscratch/lab` — dedicated storage for groups and project-specific data
  * `gscratch/scrubbed/` community-shared temporary scratch space, periodically cleaned.

Every user on Klone has access to three key storage spaces mounted under `/mmfs1/` where they can **write** *and* **read** files:

1. Home directory (`/mmfs1/home/UWNetID`)— personal, backed-up storage
2. Project/lab dedicated storage (`/gpfs/projects/group-name`) — shared, backed-up storage for research groups
3. Scrubbed storage (`/gpfs/scrubbed/some-directory`) — large, temporary scratch space for active computation

Here's a quick overview of Klone storage policies:
| Storage             | Size / Quota          | Backup          | Notes                                                                        |
| ------------------- | --------------------- | --------------- | ---------------------------------------------------------------------------- |
| Home Directory      | 10 GB per user        | Daily snapshots | Keep only configuration files here; use other spaces for data/code           |
| Project/Lab Storage | 1 TB per project/lab  | Daily snapshots |  |
| Scrubbed Storage    | Up to 100 TB per user | None            | Scratch space, purged after 60 days of inactivity; not for long-term storage |

## Practice

Let's review key storage directories on Klone and practice commands.

### 1. Your Home Directory

Your Home directory is your default location when logging into Klone. It's located at:

```bash
cd ~
/mmfs1/home/UWnetID
```
where **UWnetID** is *your* UW NetID.

We recommend storing only configuration files here and using other storage spaces for data, code, and software.

To check your current location, use:

```bash
pwd
```
To list the contents of your directory:

```bash
ls
```
To show detailed information or hidden files:

```bash
# List items with details
ls -l
# List item including hidden files
ls -a
```

### 2. Monitoring Your Storage Usage
To see how much space each subdirectory uses:

```bash
du -h -d 1
```

This command reports how much space each folder occupies and updates dynamically as you clean up files.

### 3. Moving Around — cd
The `cd` command changes your current directory. Some useful shortcuts:

```bash
cd /       # Go to the root directory
cd ~       # Go to your home directory
cd         # Also goes to home directory
cd /gpfs   # Go to the GPFS directory
cd datasets # Go to our Data Commons
ls         # List savailable datasets
cd -       # Return to your previous directory
```
Check your current location with `pwd`.

### 4. Scrubbed Storage — Our Tutorial Workspace
Scrubbed storage is temporary scratch space for active computation. It's not backed up and files are deleted automatically after **60 days** of inactivity.

Location:

```bash
/gscratch/scrubbed/
```

For this tutorial, we'll use scrubbed space as our working directory. Create a personal folder there and move into it:

```bash
mkdir /gpfs/scrubbed/$USER
cd /gpfs/scrubbed/$USER
```

You can check the contens of your working directory and the contents of the git repository at any time with:

```bash
ls
```

#### Important Note on `/gscratch/scrubbed` and Conda Environments

Because `/gscratch/scrubbed` is periodically cleaned, files that have not been modified in the last 60 days may be deleted.
We have found that if users store their Conda environment directories here, some package files may be removed over time, breaking the environment.

* Do not store Conda environments in `/gscratch/scrubbed`.
* The home directory is too small for most environments.
* We recommend using dedicated project storage for stable environment storage.

### 5. Practice: Exploring the Klone Filesystem
Let's practice a few commands to get familiar with the filesystem:

```bash
# Go to the root directory
cd /

# List top-level directories
ls

# Explore home directories
ls /gpfs/home/

# Explore scrubbed storage
ls /gpfs/scrubbed/

# Enter your scrubbed working directory for this tutuorial
cd /gpfs/scrubbed/$USER

# Return to your home directory
cd ~
pwd
```
