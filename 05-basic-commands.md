<!-- omit in toc -->
# Basic Linux Commands

In this section, we will review more commands to get you comfortable doing basic things on Hyak. Some of the data and exercises for this tutorial were sampled from [<ins>**The Unix Shell by Software Carpentry**</ins>](https://swcarpentry.github.io/shell-novice/index.html), but have been tailored to fit most Hyak users. Sampled materials are under the Copyright of Software Carpentry and are made available under the Creative Commons Attribution license (CC BY 4.0).

We'll use some commands you already know like `pwd`, `cd`, and `ls`, but we'll cover the following commands and concepts for the first time: 
- [`mkdir` or "make directory" to make an empty directory](#mkdir-or-make-directory-to-make-an-empty-directory)
- [Edit files with `nano`](#edit-files-with-nano)
- [`cat` or "concatenate" a file to print its contents](#cat-or-concatenate-a-file-to-print-its-contents)
- [`cp` or "copy" files](#cp-or-copy-files)
- [`mv` or "move" file to a new name (rename)](#mv-or-move-file-to-a-new-name-rename)
- [`rm` or "remove" a file](#rm-or-remove-a-file)
- [Wildcard `*`](#wildcard-)
- ["Redirect" output to a file with `>`](#redirect-output-to-a-file-with-)
- ["Append" output to a file with `>>`](#append-output-to-a-file-with-)
- [Search for a pattern with `grep`](#search-for-a-pattern-with-grep)
- [Use a `|` or "pipe" character to string commands together](#use-a--or-pipe-character-to-string-commands-together)
- [View your command history `history`](#view-your-command-history-history)

<!-- omit in toc -->
## Setup: preparing your tutorial workspace

You should have already completed these steps earlier in the tutorial, but before we continue, let’s make sure everyone is starting from the same place.

For the remainder of this tutorial, **your working directory will be**:

```bash
/gscratch/scrubbed/$USER/klone-onboarding-cheme599a
```
Navigate to your working directory before moving on: 

```bash
cd /gscratch/scrubbed/$USER/klone-onboarding-cheme599a
```

If this you don't have you working directory yet, [<ins>return to the Filesystem Scrubbed section</ins>](./02-filesystem.md#5-scrubbed-storage--our-tutorial-workspace) to set it up. 

## `mkdir` or "make directory" to make an empty directory 

Let's practice making a directory called "writing" in current directory and navigate into it

```bash
mkdir writing
cd writing
```

Note that `mkdir` is not limited to creating single directories one at a time. The `-p` option for "path" allows `mkdir` to create a directory with nested subdirectories in a single operation, and no error will be reported if a directory given as an operand already exists.

```bash
# make a directory called project with subdirectories data and results
# make these one directory "above" where we are now
mkdir -p ../project/data ../project/results
```

`-F` option with `ls` puts a `/` after directories to differentiate them from other objects.

```bash
ls -F ../
```

The `-R` option to the `ls` command will list all nested subdirectories within a directory. Let’s use `ls -FR` to recursively list the new directory hierarchy we just created in the project directory:

```bash
ls -FR ../project
```

> ⚠️ **WARNING:** Avoid complicated names for files and directories
> 
> - **Avoid spaces** - Spaces separate arguments on the command line, so they often cause unexpected behavior. Use `-` or `_` instead (for example, `north-pacific-gyre/` rather than `north pacific gyre/`).
> - **Don’t start names with `-` (dash)** - Anything beginning with `-` is interpreted as a command option, not a filename.
> - **Stick to safe characters** - Use letters, numbers, `.`, `-`, and `_`. Many other characters have special meanings in the shell and can cause commands to fail or behave in unexpected ways.

## Edit files with `nano`

To edit files on Klone we need to go back to basic text editors. You will not have access to a word processor, and formatting and syntax doesn't always translate from Microsoft Word or similar software to executable commands on Klone. Next, we will create a file called `draft.txt` and open it in the text editor `nano`.

First make sure you're in `/gscratch/scrubbed/$USER/klone-onboarding-cheme599a/writing`:

```bash
pwd
```

Then create and open a file called draft.txt with the command:

```bash
nano draft.txt
```

> 📝 **NOTE:** There are other text editors you could choose from. `vim` is a popular choice. `nano` is beginner friendly, so that is what we will use here.

Let's type a few lines of text.

![Screenshot of nano text editor showing draft.txt and the example text.](./img/draft_nano.png 'nano')\
*Screenshot of `nano` text editor showing draft.txt and the example text.*

Once we’re happy with our text, we can press `Ctrl`+`O` (press the `Ctrl` or `Control` key and, while holding it down, press the `O` key) to write our data to disk. We will be asked to provide a name for the file that will contain our text. Press Return to accept the suggested default of `draft.txt`.

Once our file is saved, we can use `Ctrl`+`X` to quit the editor and return to the shell.

## `cat` or "concatenate" a file to print its contents

Let's view our work. 

```bash
cat draft.txt
```

> 📝 **NOTE:** **Paths** and **Access**
>
> To access a file or directory (i.e., item) you must: 
> - be inside of the directory where the item is and provide a relative path to the item from your current directory
> - or provide an absolute path to the item

## `cp` or "copy" files

Move to top of working directory.

```bash
cd /gscratch/scrubbed/$USER
pwd
```

Copy `animals.csv` to your current directory using the shorthand `.` to mean "here"

```bash
cp /mmfs1/sw/hyak101/basics/data/animals.csv .
```

Copy a directory with all its contents using recursive copy

```bash
cp -r /mmfs1/sw/hyak101/basics/data/ .
```

## `mv` or "move" file to a new name (rename)

```bash
mv animals.csv dataset.csv
```

## `rm` or "remove" a file

> ⚠️ **WARNING:** ***`rm` permanently deletes a file. This action is irreversible.***

```bash
rm dataset.csv
```

Remove a directory with recursive `rm`.

```bash
cd klone-onboarding-cheme599a/
ls
# Use extreme caution with this command
rm -r project
```

## Wildcard `*`

Wildcards are special characters used as a shorthand. `*` is the mostly used wildcard.

```bash
cd /gscratch/scrubbed/$USER/klone-onboarding-cheme599a

# list all files
ls

# lists all files ending with .md
ls *.md

# further examples
ls /sw/hyak101/basics/*.slurm
ls /sw/hyak101/basics/locator*
ls /sw/hyak101/basics/locator_NN*
```

## "Redirect" output to a file with `>`

```bash
# list all files in current directory and redirect result to a file ls.out
ls -a > ls.out
cat ls.out
```

> ⚠️ **WARNING:** If the file already exists, it will be overwritten.

## "Append" output to a file with `>>`

```bash
# list all files in current directory in long format and append result to ls.out
ls -l >> ls.out
cat ls.out
```

Using `>>` can avoid overwriting a file.

## Search for a pattern with `grep`

`grep` finds and prints lines in files that match a pattern

```bash
cat ls.out
grep slurm ls.out
```

Only the lines containing "slurm" will print out.

## Use a `|` or "pipe" character to string commands together

Alternatively, files ending with "slurm" can be printed by using one line of code:

```bash
ls -la | grep "slurm"
```

The standard output of `ls -la` is sent directly as the standard input to `grep`.

## View your command history `history`

```bash
history
```

Use `history`, `|`, and `grep` together to find all times the `cat` command was used.

```bash
history |grep cat
```

> 💡 **TIPS:** Use the `--help` flag or the `man` command to view the help message or system documentation of a command.