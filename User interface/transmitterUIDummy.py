from customtkinter import *
import os
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Import Image and ImageTk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time
from tkinter import filedialog
import sys
from sympy import true
import tkinter.scrolledtext as scrolledtext  # For scrollable terminal output


class TransmitterApp(CTk):
    def __init__(self):
        super().__init__()
        self.path=os.path.dirname(os.path.abspath(__file__))

        self.geometry("700x560")
        self.resizable(0, 0)
        self.title("Transmitter")

        # Initialize variables
        self.file_path = None
        self.preview_photo = None
        self.process = None

        # Initialize UI
        self.create_sidebar()
        self.create_main_frame()

    def create_sidebar(self):
        sidebar_frame = CTkFrame(master=self, fg_color="#522B5B", width=150, height=560, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        back_img_data = Image.open("User interface/src/back.png")
        back_img = CTkImage(dark_image=back_img_data, light_image=back_img_data)

        back_button = CTkButton(
            master=sidebar_frame,
            image=back_img,
            text="Back to Home",
            fg_color="transparent",
            font=("Arial Bold", 14),
            hover_color="#654F6C",
            anchor="w",
            command=self.go_back_to_home
        )
        back_button.pack(anchor="center", ipady=5, pady=(60, 0))

        antenna_img_data = Image.open("User interface/src/antenna.png")
        antenna_img = CTkImage(dark_image=antenna_img_data, light_image=antenna_img_data, size=(100, 100))
        CTkLabel(master=sidebar_frame, text="", image=antenna_img).pack(pady=(120, 0), anchor="center")

    def create_main_frame(self):
        frame = CTkFrame(master=self, width=550, height=560, fg_color="white")
        frame.pack_propagate(0)
        frame.pack(side="right", fill="both", expand=True)

        select_file_button = self.create_button(
            master=frame,
            text="Select File",
            command=self.select_file
        )
        select_file_button.pack(pady=(20, 10), anchor="center")

        send_button = self.create_button(
            master=frame,
            text="Send",
            command=self.send_file
        )
        send_button.pack(pady=(10, 20), anchor="center")

        self.bottom_box = CTkFrame(master=frame, width=500, height=200, fg_color="#DFB6B2")
        self.bottom_box.pack( fill="both", expand=True, padx=20, pady=20)

        self.preview_label = CTkLabel(
            master=self.bottom_box,
            text="",
            font=("Arial", 14),
            text_color="#522B5B",
            wraplength=480
        )
        self.preview_label.pack(pady=(10, 10), anchor="center")

        # Terminal output window
        self.terminal_output = scrolledtext.ScrolledText(
            master=frame,
            wrap=tk.WORD,
            font=("Courier", 10),
            bg="#DFB6B2",
            fg="#000000",
            height=10
        )
        self.terminal_output.pack(fill="both", expand=True, pady=(0,10), padx=(10,10))
        self.terminal_output.configure(state="disabled")  # Initially non-editable

        # Start a thread to read the terminal output
        threading.Thread(target=self.terminal_output, daemon=True).start()

    def create_button(self, master, text, command):
        button = CTkButton(
            master=master,
            text=text,
            fg_color="#854F6C",
            hover_color="#522B5B",
            text_color="#190019",
            font=("Arial Bold", 20),
            width=180,
            height=40,
            command=command
        )
        button.bind("<Enter>", lambda e: self.on_hover(button, "#522B5B", "#FBE4D8"))
        button.bind("<Leave>", lambda e: self.on_leave(button, "#854F6C", "#190019"))
        return button

    def on_hover(self, button, hover_color, text_color):
        button.configure(fg_color=hover_color, text_color=text_color)

    def on_leave(self, button, original_color, text_color):
        button.configure(fg_color=original_color, text_color=text_color)

    def go_back_to_home(self):
        self.destroy()
        subprocess.run([sys.executable, "User interface/home.py"])  # Adjust the path to your home.py file
    
    def format_file_size(self, size_bytes):
        """Convert file size to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0

    def select_file(self):
        self.selected_file_path = filedialog.askopenfilename()
        if self.selected_file_path:
            # Extract file name
            file_name = os.path.basename(self.selected_file_path)

            # Get file size
            file_size = os.path.getsize(self.selected_file_path)
            size_str = self.format_file_size(file_size)

            # Update the preview label with file name and size on separate lines
            self.preview_label.configure(
                text=f"File Name: {file_name}\nFile Size: {size_str}"
            )

    def send_file(self):
        """Send file using transmitter.py and display terminal output in the app."""
        try:
            def encrypt_data(data, key, iv):
                cipher = AES.new(key, AES.MODE_CBC, iv)
                return cipher.encrypt(pad(data, AES.block_size))

            def add_preamble():
                binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
                file_path = self.selected_file_path
                file_name = os.path.basename(file_path).encode()

                with open(file_path, 'rb') as file:
                    plaintext = file.read()
                preamble = binarypreamble * 3000
                detect_sequence = b'sts'
                end_sequence = b'end'

                key = b'Sixteen byte key'
                iv = b'This is an IV456'
                encrypted_plaintext = encrypt_data(plaintext, key, iv)

                with open('./Transiver/File Transiver/tx.tmp', 'wb') as output_file:
                    output_file.write(preamble + detect_sequence + file_name + b'|||' + plaintext + end_sequence + preamble)

            # Adds the preamble
            add_preamble()

            # Resolve the path to the script
            transmitter_path = os.path.abspath(os.path.join(self.path, '../Transiver/File Transiver/Transmitter.py'))
            print(transmitter_path)

            # Function to read subprocess output
            def read_output(process):
                while process.poll() is None:  # While the process is running
                    output_line = process.stdout.readline()
                    if output_line:
                        self.terminal_output.configure(state="normal")
                        self.terminal_output.insert(tk.END, output_line)
                        self.terminal_output.see(tk.END)
                        self.terminal_output.configure(state="disabled")
                
                # Capture any remaining output after process ends
                remaining_output, errors = process.communicate()
                if remaining_output:
                    self.terminal_output.configure(state="normal")
                    self.terminal_output.insert(tk.END, remaining_output)
                    self.terminal_output.see(tk.END)
                    self.terminal_output.configure(state="disabled")
                if errors:
                    self.terminal_output.configure(state="normal")
                    self.terminal_output.insert(tk.END, errors)
                    self.terminal_output.see(tk.END)
                    self.terminal_output.configure(state="disabled")

            # Remove existing progress bar if it exists
            if hasattr(self, 'progress_bar'):
                self.progress_bar.pack_forget()
                del self.progress_bar

            # Remove existing status label if it exists
            if hasattr(self, 'status_label'):
                self.status_label.pack_forget()
                del self.status_label

            # Create and pack the progress bar
            self.progress_bar = CTkProgressBar(master=self.bottom_box, width=400)
            self.progress_bar.pack(pady=(10, 10), anchor="center")
            self.progress_bar.set(0)

            # Create and pack the status label
            self.status_label = CTkLabel(master=self.bottom_box, text="Initializing...", font=("Arial", 14), text_color="#522B5B")
            self.status_label.pack(pady=(5, 10), anchor="center")

            # Function to start the subprocess
            def run_transmitter():
                self.process = subprocess.Popen(
                    ['python', transmitter_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                # Start reading the output in another thread
                threading.Thread(target=read_output, args=(self.process,), daemon=True).start()

            def update_progress_bar():
                start_time = time.time()
                while time.time() - start_time < 8.5:
                    self.progress_bar.set((time.time() - start_time) / 8.5)
                    time.sleep(0.1)
                self.progress_bar.set(1.0)
                self.status_label.configure(text="Sending...")

            threading.Thread(target=run_transmitter, daemon=True).start()
            threading.Thread(target=update_progress_bar, daemon=True).start()

            threading.Thread(target=update_progress_bar, daemon=True).start()

        except Exception as e:
            self.terminal_output.configure(state="normal")
            self.terminal_output.insert(tk.END, f"Error: {str(e)}\n")
            self.terminal_output.see(tk.END)
            self.terminal_output.configure(state="disabled")

    def read_terminal_output(self):
        """Read the subprocess output and display it in the terminal window."""
        while self.process.poll() is None:  # While the process is still running
            line = self.process.stdout.readline()
            if line:
                self.terminal_output.configure(state="normal")
                self.terminal_output.insert(tk.END, line)
                self.terminal_output.see(tk.END)  # Auto-scroll to the latest line
                self.terminal_output.configure(state="disabled")

        # Capture any remaining output after the process ends
        remaining_output, errors = self.process.communicate()
        if remaining_output:
            self.terminal_output.configure(state="normal")
            self.terminal_output.insert(tk.END, remaining_output)
            self.terminal_output.see(tk.END)
            self.terminal_output.configure(state="disabled")
        if errors:
            self.terminal_output.configure(state="normal")
            self.terminal_output.insert(tk.END, errors)
            self.terminal_output.see(tk.END)
            self.terminal_output.configure(state="disabled") 

if __name__ == "__main__":
    app = TransmitterApp()
    app.mainloop()
