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

![Diagrammatic representation of the Klone filesystem directory tree. The root directory appears at the top and contains several subdirectories. A truncated view highlights the mmfs1 directory and selected subdirectories within it, including home for user home directories, sw for shared software and scripts, and gscratch for project and lab group storage. Some directories are shown in blue to indicate they are also accessible via symbolic links from shorter top-level paths.](/img/filesystem_klone.jpg 'filesystem')

*Simplified view of the Klone filesystem hierarchy. The root directory (`/`) at the top contains all subdirectories. This diagram highlights `/mmfs1` and commonly used paths within it, including user home directories (`/mmfs1/home`), shared software and scripts (`/mmfs1/sw`), project and lab group storage (`/mmfs1/gscratch`), and common datasets (`/mmfs1/data`). Directories shown in blue indicate locations that are also available through symbolic links for convenience.*

As shown above, the Klone filesystem is organized under the root directory `/`. Within it, `/mmfs1/` contains several key subdirectories:

- `/mmfs1/home/` — individual user home directories for configuration, small scripts and lightweight code.
> ⚠️ **WARNING:** Home directories on Klone have limited quota (**10 GB**). Active research data, training datasets, and large outputs should be stored in project or scrubbed storage, not in $HOME. 
- `/mmfs1/gscratch/` — shared scratch storage
  - `/mmfs1/gscratch/lab` — dedicated storage for groups and project-specific data. Variable total capacity based on hardware holdings.
  - `/mmfs1/gscratch/scrubbed/` — free community storage for temporary, high-capacity workloads. Data stored in scrubbed locations will be automatically removed after 21 days of inactivity, so it should only be used for intermediate or reproducible data. User limit of 10TB, but amount is not guarenteed and may not be available.
- `/mmfs1/sw/` — centrally managed shared applications and tools, and user-contributed softwares under `sw/contrib`
- `/mmfs1/data/` — curated public or shared research datasets. Groups can nominate datasets for storage under following our [**<ins>Data Commons</ins>**](https://hyak.uw.edu/docs/data-commons/requirements).

> 📝 **NOTE: No storage location on Klone is backed up.**
> 
> This includes home directories, group storage, and scrubbed spaces.
> 
> Users are responsible for backing up any data they wish to preserve. We strongly recommend maintaining copies of important data outside of Klone.

> 📝 **NOTE: Symbolic Links on Klone**
>
> On Klone, some commonly used directories have symbolic links (also called symlinks) that provide shorter, easier-to-type paths.
>
> For example, `/mmfs1/gscratch` and `/gscratch` refer to the same location.
> 
> Symbolic links do not duplicate data. Instead, they act as pointers to the original directory. You can safely use either path when navigating the filesystem or writing job scripts.
> ```bash
> $ ls -l
> lrwxrwxrwx    1 root root     15 Mar 10 05:48 gscratch -> /mmfs1/gscratch
> ```
> 
> ***You may see multiple paths that appear different but resolve to the same location. This is expected behavior on Klone and is used to improve usability.***

## Basic Commands

Linux provides a small set of commands that you'll use constantly to navigate the file system. In this section, we will practice using these common commands to move around Hyak Klone.

### 1. `pwd`: Where Am I?

The `pwd` command prints your current directory.

```bash
pwd
```

When you log in to Klone, you should see something like:

```bash
/mmfs1/home/UWnetID
```
where **UWnetID** is *your* UW NetID.

This is the absolute path to your Home directory. An absolute path always starts at the root directory (`/`) and describes a full address to a location on the system.

### 2. `cd`: Moving Between Directories

The `cd` command changes your current directory.

For example, to move into a shared tutorial directory:

```bash
cd /mmfs1/sw/hyak101/basics
```

Your prompt will update to reflect your new location:

```bash
[UWNetID@klone-login01 basics]$
```

To return to your Home directory:

```bash
ch ~
```

> 💡 **TIPS: Useful `cd` Shortcuts**
> - `cd ~` or `cd` Go to your Home directory
> - `cd -` or `cd ..` Go back to your previous directory

### 3. `ls`: Listing Directory Contents

The `ls` command shows the contents of a directory.

```bash
ls
```

If your Home directory is new or mostly empty, you may see little or no output.

To explore the broader filesystem, try listing the root directory:

```bash
cd /
ls
```

You'll see many system directories, including `mmfs1`.

Now list what's inside `mmfs1`:

```bash
ls /mmfs1
```

This includes:
- home/ — user home directories
- gscratch/ — group and project storage
- sw/ — shared software and scripts
- data/ - common datasets

You do not need to be inside a directory to list its contents. You can provide a path directly to `ls`.

> 💡 **TIPS: Useful `ls` Options:**
> - `ls -l` Lists long format (permissions, size, owner, date)
> - `ls -a` Lists all items including hidden files. Hidden files begin with a `.` (for example, `.bashrc`). These are common in your Home directory and usually control shell behavior.

### 4. Node vs. Filesystem Location

Your command prompt shows two kinds of location.

```bash
hostname
```

This prints the name of the login node you're connected to (e.g., `klone-login01`).

### 5. Scrubbed Storage — Our Tutorial Workspace

Scrubbed storage is temporary scratch space for active computation. It's not backed up and files are deleted automatically after **21 days** of inactivity.

Location:

```bash
/gscratch/scrubbed/
```

For this tutorial, we'll use scrubbed space as our working directory. Create a personal folder there and move into it:

```bash
mkdir /gscratch/scrubbed/$USER
cd /gscratch/scrubbed/$USER
```

While we're at it, le'ts clone the git repository for this tutorial, we'll use some of the files later.

```bash
git clone https://github.com/UWrc/klone-onboarding-cheme599a.git
```

You can check the contens of your working directory and the contents of the git repository at any time with:

```bash
ls
ls klone-onboarding-cheme599a
```