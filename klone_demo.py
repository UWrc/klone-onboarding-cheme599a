import os
import platform
import socket
import subprocess


def print_header():
    print("▶️ Starting Klone demo job...")
    print(f"Hostname: {socket.gethostname()}")
    print(f"User: {os.environ.get('USER', 'unknown')}")
    print(f"Python version: {platform.python_version()}")
    print()


def check_gpu():
    print("Checking GPU availability with nvidia-smi...")
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total,memory.used",
                "--format=csv,noheader"
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        output = result.stdout.strip()
        if output:
            print("GPU detected:")
            for i, line in enumerate(output.splitlines()):
                print(f"  GPU {i}: {line}")
        else:
            print("nvidia-smi ran successfully, but no GPU information was returned.")
    except FileNotFoundError:
        print("nvidia-smi not found. This node may not have NVIDIA GPUs available.")
    except subprocess.CalledProcessError as e:
        print("Unable to query GPU information.")
        if e.stderr:
            print(e.stderr.strip())
    print()


def main():
    print_header()
    check_gpu()
    print("✅ Completed successfully.")


if __name__ == "__main__":
    main()