import subprocess


def run_tasklist():
    # Run tasklist command to list running processes
    result = subprocess.run("tasklist", shell=True, capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Print the output of the tasklist command
        print(result.stdout)
    else:
        # Print an error message if the command failed
        print("Error: Unable to run tasklist command.")


if __name__ == "__main__":
    run_tasklist()
