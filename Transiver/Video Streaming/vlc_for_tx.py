#This modules will start the VLC in ubuntu

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
    # Example command to run
    cmd = r'vlc v4l2:///dev/video0 --sout="#transcode{vcodec=mp2v,vb=600,scale=0.5,acodec=none,scodec=none}:duplicate{dst=file{dst=./im.ts,no-overwrite},dst=display}" --sout-all --sout-keep'
    thread = run_in_thread(cmd)

    # Do other tasks while the command runs
    # Optionally, wait for the thread to complete
    # thread.join()
print("vlc started.")