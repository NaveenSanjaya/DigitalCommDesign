from customtkinter import *
from PIL import Image, ImageTk
import time
import subprocess
import sys
import os
from tkinter import filedialog
import tkinter as tk


class StreamApp(CTk):
    def __init__(self):
        super().__init__()
        self.path=os.path.dirname(os.path.abspath(__file__))

        self.geometry("700x560")
        self.resizable(0, 0)
        self.title("Transmitter")

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

        server_button = self.create_button(
            master=frame,
            text="Server",
            command=self.server
        )
        server_button.pack(pady=(20, 10), anchor="center")

        viewer_button = self.create_button(
            master=frame,
            text="Viewer",
            command=self.viewer
        )
        viewer_button.pack(pady=(10, 20), anchor="center")

        bottom_box = CTkFrame(master=frame, width=500, height=200, fg_color="#DFB6B2")
        bottom_box.pack(side="bottom", fill="both", expand=True, padx=20, pady=20)

        self.streaming_label = CTkLabel(
            master=bottom_box,
            text="",
            font=("Arial", 14),
            text_color="#522B5B"
        )
        self.streaming_label.pack(pady=(10, 10), anchor="center")

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
        subprocess.run([sys.executable, "User interface/home.py"])

    def server(self):
        # Resolve the path to the script
        reciver_path = os.path.abspath(os.path.join(self.path, '../Transiver/Video Streaming/VideoTransmitter.py'))
        # Start the subprocess
        subprocess.Popen(['python', reciver_path],text=True)

    def viewer(self):
        # Resolve the path to the script
        reciver_path = os.path.abspath(os.path.join(self.path, '../Transiver/Video Streaming/VideoReciver.py'))
        # Start the subprocess
        subprocess.Popen(['python', reciver_path],text=True)

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
    app = StreamApp()
    app.mainloop()
