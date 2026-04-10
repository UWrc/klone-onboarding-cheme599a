# Logging In to Hyak Klone

Accessing Klone through the command line allows you to interact directly with the cluster — submitting jobs, managing files, and running software. When you log in using SSH, you're opening a secure terminal session on one of the login nodes. From here, you can explore the filesystem, prepare scripts, and submit workloads to compute nodes.

## Logging in to Klone

Once you have a terminal (shell) open on your local machine, log in to Klone by running the following command. Replace `UWNetID` with your UW NetID.

```bash
ssh UWNetID@klone.hyak.uw.edu
```

You'll be prompted for your UW NetID password (*Note: your Hyak password is the same password for all your UW Services*), followed by your Duo two-factor authentication method:

```bash
Password: 
Duo two-factor login for UWNetID

Enter a passcode or select one of the following options:

 1. Duo Push to XXX-XXX-1234
 2. Phone call to XXX-XXX-1234

Passcode or option (1-2): 1
Success. Logging you in...
```

If successful, you'll see a welcome banner like this:

```bash
     _    _                    _                 _
    | | _| | ___  _ __   ___  | |__  _   _  __ _| | __
    | |/ / |/ _ \| '_ \ / _ \ | '_ \| | | |/ _` | |/ /
    |   <| | (_) | | | |  __/ | | | | |_| | (_| |   <
    |_|\_\_|\___/|_| |_|\___| |_| |_|\__, |\__,_|_|\_\
                                     |___/

This login node is meant for interacting with the job scheduler and 
transferring data to and from KLONE. Please work by requesting an 
interactive session on (or submitting batch jobs to) compute nodes.
```

> ⚠️ **WARNING:** Too many incorrect login attempts may result in a temporary IP ban lasting up to an hour.

---

> 💡 **Common Login Issues**
>
> If you're having trouble logging in to Hyak, the issues below account for most problems we see.
> 
> **1. Lost or Expired Access**
> 
> If your login attempt fails even though your password and 2FA are correct, your Hyak access may have expired or been removed.
> - Contact **UWIT Research Computing** or your **Hyak account administrator** for your research group to confirm your access.
> - Students using shared or instructional allocations (such as STF) may need to [**reapply for access**](https://depts.washington.edu/uwrcc/hyak_access/).
>   - In many cases, STF access does not automatically renew between quarters.
>
> **2. Incorrect Username or Password**
> 
> Be sure that:
> - You are using your **UW NetID** (not an email address)
> - Your password is typed correctly (passwords are not shown as you type)
> 
> ***Too many incorrect login attempts may result in a temporary IP ban lasting up to an hour.***
>
> If you believe you may have triggered a temporary ban, wait and try again later.
> 
> **3. Network Issues (On Campus)**
>
> If you are connecting from campus, make sure you are using the [**`eduroam`**](https://uwconnect.uw.edu/it?id=kb_article_view&sysparm_article=KB0034255#howtouse) wireless network.
> - The **“University of Washington”** network is known to be less stable for SSH connections
> - Switching to **eduroam** often resolves intermittent login failures
>
> **4. Internet Connectivity Problems**
>
> Unstable internet connections—both on campus and off campus—can interfere with SSH logins.
>
> If login fails unexpectedly:
> - Check your internet connection
> - Wait a few minutes and try again
> - Try reconnecting from a different network if possible
> 
> **Still Having Trouble?**
> 
> If your login issues persist after checking the items above, please contact UW support:
> 
> **Email:** help@uw.edu  
> **Subject line:** "Hyak login issue" \
> Including “Hyak” in the subject line helps route your request to the appropriate support team.

---

## What Is a Shell?

The shell is a program that allows you to interact with a computer by typing commands. On Hyak, the shell is your primary way of navigating the filesystem, launching programs, and preparing work to run on compute nodes.

When you use `ssh` to log in to Klone or Tillicum, you are connected to a shell called Bash (the <ins>**B**</ins>ourne <ins>**A**</ins>gain <ins>**SH**</ins>ell). If you successfully logged in and see text waiting for input, you are looking at a shell.

***Think of the shell as your view into the cluster.***

### The Command Prompt

When you log in, you'll see a prompt that looks something like this:

```bash
[UWNetID@klone-login01 ~]$
```

Let's break this down:
- **UWNetID** — your username on Hyak
- **klone-login01** (or similar) — the login node you're connected to. Login nodes are the "front door" of the cluster. All users start here.
- **~** — the tilde symbol is a short hand for your home directory; this section of your command prompt will change as you traverse the filesystem in the next section.
- **$** — indicates the shell is ready for a command.

In Linux, the term **directory** is used instead of folder. While graphical interfaces often use "folder," "directory" is the correct term in the command-line environment.

We will discuss the filesystem, directories, and storage locations in more detail in the next section.

> 📝 **A Note on Login Nodes**
>
> Login nodes are shared by all users and are intended for:
> - Editing files
> - Navigating directories
> - Transferring data
> - Submitting jobs to the scheduler
>
> ***Compute- or memory-intensive work should not be run on login nodes.*** **Arbiter** is the tool which automates login node monitoring and enforces usage limits to ensure stability and ensure fair access.
>
> **Arbiter monitors resource usage on login nodes and will:**
> - Slow or halt processes that exceed permitted thresholds.
> - Terminate processes outright if necessary.
> 
> You will learn how to request compute resources later in this tutorial.