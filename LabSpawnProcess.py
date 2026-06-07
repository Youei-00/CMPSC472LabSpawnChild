import subprocess

def main():
    try:
        # Hard-coded processes (constant variables)
        PROCESS_1 = "notepad.exe"
        PROCESS_2 = "calc.exe"

        # Start child processes
        child1 = subprocess.Popen(PROCESS_1)
        print(f"Started {PROCESS_1} with PID {child1.pid}")

        child2 = subprocess.Popen(PROCESS_2)
        print(f"Started {PROCESS_2} with PID {child2.pid}")

    except Exception as e:
        print("Error starting child processes:", e)
        return

    print("Parent process waiting for child processes to exit...")

    # Wait for first child to exit
    child1.wait()
    print(f"{PROCESS_1} has exited.")

    # Wait for second child to exit
    child2.wait()
    print(f"{PROCESS_2} has exited.")

    print("Both child processes have ended. Parent exiting.")

if __name__ == "__main__":
    main()