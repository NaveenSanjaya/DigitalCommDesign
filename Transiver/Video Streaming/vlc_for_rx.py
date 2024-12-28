import threading
import subprocess

def run_command(command):
    """Function to run a terminal command."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(f"Command Output:\n{result.stdout}")
        if result.stderr:
            print(f"Command Error:\n{result.stderr}")
    except Exception as e:
        print(f"Error running command: {e}")

def run_in_thread(command):
    """Function to run the command in a separate thread."""
    thread = threading.Thread(target=run_command, args=(command,))
    thread.start()
    return thread

if __name__ == "__main__":
    # Command to open VLC and listen to udp://@:2000
    cmd = r'vlc udp://@:2000'
    thread = run_in_thread(cmd)

    # Do other tasks while the command runs
    # Optionally, wait for the thread to complete
    # thread.join()
    print("VLC started and listening to udp://@:2000.")
