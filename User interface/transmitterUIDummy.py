from customtkinter import *
from PIL import Image, ImageTk
import time
import subprocess
import sys
import os
from tkinter import filedialog


class TransmitterApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x560")
        self.resizable(0, 0)
        self.title("Transmitter")

        # Initialize variables
        self.file_path = None
        self.preview_photo = None

        # Initialize UI
        self.create_sidebar()
        self.create_main_frame()

    def create_sidebar(self):
        sidebar_frame = CTkFrame(master=self, fg_color="#522B5B", width=150, height=560, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        back_img_data = Image.open("User interface/back.png")
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

        antenna_img_data = Image.open("User interface/antenna.png")
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
        select_file_button.pack(pady=(10, 5), anchor="center")

        send_button = self.create_button(
            master=frame,
            text="Send",
            command=self.send_file
        )
        send_button.pack(pady=(10, 5), anchor="center")

        stream_button = self.create_button(
            master=frame,
            text="Stream",
            command=None
        )
        stream_button.pack(pady=(10, 5), anchor="center")

        bottom_box = CTkFrame(master=frame, width=500, height=200, fg_color="#DFB6B2")
        bottom_box.pack(side="bottom", fill="both", expand=True, padx=20, pady=20)

        self.preview_label = CTkLabel(
            master=bottom_box,
            text="",
            font=("Arial", 14),
            text_color="#522B5B",
            wraplength=480
        )
        self.preview_label.pack(pady=(10, 10), anchor="center")

        self.progress_bar = CTkProgressBar(
            master=bottom_box,
            width=300,
            height=20,
            progress_color="#854F6C"
        )
        self.progress_bar.set(0)
        self.progress_bar.pack_forget()

        self.sending_label = CTkLabel(
            master=bottom_box,
            text="",
            font=("Arial", 14),
            text_color="#522B5B"
        )
        self.sending_label.pack(pady=(10, 10), anchor="center")

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

    def select_file(self):
        file_types = [
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Audio files", "*.wav *.mp3 *.ts"),
            ("Image files", "*.png *.jpg *.jpeg"),
            ("Video files", "*.mp4 *.avi")
        ]

        self.file_path = filedialog.askopenfilename(filetypes=file_types)
        if self.file_path:
            self.preview_label.configure(image="", text=f"Selected File: {os.path.basename(self.file_path)}")
            self.sending_label.configure(text="")

            if self.file_path.endswith('.txt'):
                with open(self.file_path, 'r') as file:
                    content = file.read()
                self.preview_label.configure(text=content, wraplength=480)

            elif self.file_path.endswith(('.wav', '.mp3')):
                img_data = Image.open("User interface/audio.png")
                img = CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))
                self.preview_label.configure(image=img, text="Audio file selected", compound="top", wraplength=480)

            elif self.file_path.endswith(('.png', '.jpg', '.jpeg')):
                image = Image.open(self.file_path)
                image.thumbnail((200, 200), Image.LANCZOS)
                self.preview_photo = ImageTk.PhotoImage(image)
                self.preview_label.configure(image=self.preview_photo, text="")

            elif self.file_path.endswith(('.mp4', '.avi', '.ts')):
                img_data = Image.open("User interface/video.png")
                img = CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))
                self.preview_label.configure(image=img, text="Video file selected", compound="top", wraplength=480)

    def send_file(self):
        if self.file_path:
            self.sending_label.configure(text="Sending file...")
            self.progress_bar.set(0)
            self.progress_bar.pack(pady=(10, 20), anchor="center")

            def update_progress_bar():
                for i in range(101):
                    self.progress_bar.set(i / 100)
                    self.update_idletasks()
                    time.sleep(0.05)

                self.sending_label.configure(text="File sent")

            self.after(0, update_progress_bar)


if __name__ == "__main__":
    app = TransmitterApp()
    app.mainloop()
