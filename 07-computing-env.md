# Computing Environment

Hyak Klone provides a flexible software environment for research computing. You can run software through modules (via Lmod) or containers (via Apptainer). 

## Modules

Hyak uses the [Lmod](https://lmod.readthedocs.io/en/latest/) environment module system to manage software.

Each loaded module dynamically modifies your shell environment (e.g. `PATH`, `LD_LIBRARY_PATH`) so that the corresponding executables and libraries become available.

Instead of manually editing environment variables, you simply load or unload modules.

### Understand Your Environment

When you log in, your shell environment combines: 
- System defaults — environment variables and functions defined globally for all users.
- User customizations — variables or aliases defined in your startup files (e.g., `$HOME/.bashrc`, `$HOME/.bash_profile`).
- Loaded modules — software stacks that modify your environment dynamically.

Two especially important environment variables are:
- `PATH` — a colon-separated list of directory paths that the system searches for executables.
- `LD_LIBRARY_PATH` — a similar list where the system looks for shared libraries.

View the value of the `PATH` environment variable:
```bash
echo $PATH
```

When you load a module, it typically ***prepends*** new paths to these variables so your system uses the correct version of software.

### What is Lmod?

Lmod is a Lua-based implementation of the environment modules system. Through modulefiles, it allows you to:
- Switch between different software versions
- Maintain software stacks
- Use compiler/MPI-compatible builds
- Avoid manual environment configuration

Lmod supports hierarchical module structures through `MODULEPATH`, which help prevent incompatible software combinations.

> 📝 **NOTE:** **On Klone, module commands are disabled on login nodes.** Request a compute node before searching or loading any modules.

### Core Module Commands

The module command sets the appropriate environment variable independent of your shell.

| Command | Description|
|:-----|:-----|
| `module list` | List active modules in the current environment |
| `module avail` | List available modules in the current environment |
| `module spider [module]`| Search all installed modules (deep search across all module hierarchies) |
| `module load [modules]` | Load modules |
| `module swap [module1] [module2]` | Replace `module1` with `module2` |
| `module unload [modules]` | Unload specific modules |
| `module purge` | Unload ***all*** modules from the current environment |
| `module show [module]` | Show functions performed by loading module |
| `module help [module]` | Show module-specific help message |
| `module use [-a] [path]` | Prepend or append path to `MODULEPATH` |

Lmod provides a convenient shortcut command [`ml`](https://lmod.readthedocs.io/en/latest/010_user.html#ml-a-convenient-tool) for the `module` command.

> 💡 **TIP:** `ml` can be used instead of module, module load, or module list depending on the situation.

| Example | Equivalent|
|:-----|:-----|
| `ml` | `module list` |
| `ml [module]` | `module load [module]` |
| `ml -[module]` | `module unload [module]` |
| `ml avail` | `module avail` |

Any module sub-commands (e.g., avail, spider, show, etc.) can be written as `ml subcommand [args]`.

### Find Modules

**Use `module avail`**

List all modules visible in your current environment after starting an interactive session:

```bash
salloc -A uwit -p ckpt-all -N 1 --time=2:00:00
module avail
```

> 💡 **TIP:** **Klone** provides a shared directory under `/sw/contrib/mylab-src` where each group can install software intended for shared use across Klone users. See the [Hyak Documentation](https://hyak.uw.edu/docs/tools/modules#how-do-i-create-shared-lmod-modules-on-klone) for instructions on creating and managing user-contributed Lmod modules.

To narrow results, for instance, if you want to see all `gcc` modules:

```bash
module avail gcc
```

> 📝 **NOTE:** `module avail` doesn't show modules from all trees in the hierarchical system, which is the case for **Tillicum**.

**Use `module spider` (Recommended)**

The `module spider` command performs a **deep search** across all module hierarchies, even ones not currently visible:

```bash
module spider cuda
```

For detailed loading instructions:

```bash
module spider cuda/12.9.1
```

The above output also indicates a modulefile's complete name includes its name and version. An installed application can have several versions. If dependencies exist, `module spider` will also show them.

> 📝 **NOTE:** `module spider` is the most reliable way to search installed software and learn what prerequisites must be loaded first. **Always use `module spider` instead of `module avail` to find out how to `module load`.**

### Load Modules on Klone

To load a module on Klone, run:

```bash
module load cuda/12.9.1
```

> ⚠️ **WARNING:** Do not include `module load` commands in your startup files (e.g., `$HOME/.bashrc`, `$HOME/.bash_profile`). This can cause conflicts when switching environments in batch jobs and interactive sessions.

## Conda Environments

Conda allows you to create isolated environments that include specific versions of Python, libraries, and tools. This is essential in HPC environments, where reproducibility and dependency control are critical.

If you’re new to Conda, you may find this helpful: [Conda Cheatsheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)

### Load Conda Module

Hyak provides a minimal Miniforge (Conda) installation that you can utilize to build custom Conda environment. You must load it before using `conda`:

```bash
salloc -A uwit -p ckpt-all -N 1 --time=2:00:00
module load conda
```

The `conda` command becomes available now.

> 📝 **NOTE:** For Klone users, be sure to run the `module load` command on a compute node. After loading the system Conda module, you do not need to run `conda init` or modify your shell startup file (`$HOME/.bashrc`). The module handles environment setup for you.

### Create and Manage Conda Environments

**Choose Where to Store Environments and Packages (Important)**

By default, the system Conda stores environments in your home directory (`$HOME/.conda/envs`). However, your home directory on Hyak has a **10 GB** quota, which is often insufficient. 

We recommend installing Conda environments to your **project directory** `/gscratch/<myproject>/<myfolder>`

**Option A (Recommended): Configure Defaults in `$HOME/.condarc`**

To store all of your environments and package caches in custom locations by default, edit (or create) your Conda configuration file:

```bash
nano ~/.condarc
```

Add to the file opened:

```yaml
envs_dirs:
  - /gscratch/<myproject>/<myfolder>/conda/envs
pkgs_dirs:
  - /gscratch/<myproject>/<myfolder>/conda/pkgs
always_copy: true
```

Replace \<myproject\> and \<myfolder\> with real paths. Save (^O) and exit (^X) before continue in the shell.

**Option B: Use `--prefex` for Explicit Control**

Manually set the path to your Conda environment by `--prefix` and always activate your Conda environment with full path.

```bash
module load conda
conda create --prefix /gscratch/<myproject>/<myfolder>/myenv python=3.12
conda activate /gscratch/<myproject>/<myfolder>/myenv
```

This gives you complete control over where each environment lives.

### Create a Conda environment

For example, create a custom Conda environment named `myenv` with Python 3.12 and other scientific packages installed:

```bash
module load conda
conda create -n myenv python=3.12 numpy scipy pandas
```

Activate the environment:

```bash
conda activate myenv
```

Once activated, all `python`, `pip`, and `conda install` commands apply only to this environment. 

Conda has several default channels that will be used first for package installation with `conda install`. You can use another channel beyond the default channels, but we suggest that you select your channel carefully.

### Install Packages with `pip`

You can use `pip` inside a Conda environment to install Python packages. Anaconda provides some [best practices](https://www.anaconda.com/blog/using-pip-in-a-conda-environment) for using `pip` with Conda. Our suggested use of pip is inside a conda environment.

Example:
```bash
module load conda
conda activate myenv
pip install seaborn
```

This ensures that `pip` installs packages into the active Conda environment — **not globally** — making it easy to clean up completely when you are done.

See the [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/) for more information.

> 💡 **Best practices on Hayk:**
> - Use separate environments for different projects
> - Use `pip install` inside a Conda environment
> - Install CUDA-aware packages on a **GPU node**, with compatible CUDA module/version loaded before installation.

## Containers (Optional)

Hyak supports Apptainer containers for portable, isolated software stacks. For complex GPU workflows, portable software stacks, or highly reproducible research, consider using Apptainer containers instead of Conda.

Useful resources:
- [NVIDIA's NGC Catalog](https://catalog.ngc.nvidia.com/?filters=&orderBy=weightPopularDESC&query=&page=&pageSize=) provides prebuilt containers with CUDA and NVIDIA drivers configured
- [Hyak Containers Documentation](https://hyak.uw.edu/docs/tools/containers)
- [Klone Containers Tutorial](https://hyak.uw.edu/docs/hyak101/containers/syllabus)
- [Tillicum Containers Tutorial](https://github.com/UWrc/tillicum-containers/)