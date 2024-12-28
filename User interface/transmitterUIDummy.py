from customtkinter import *
import customtkinter as ctk
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
        select_file_button.pack(pady=(20, 10), anchor="center")

        send_button = self.create_button(
            master=frame,
            text="Send",
            command=self.send_file
        )
        send_button.pack(pady=(10, 20), anchor="center")

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

        self.selected_file_path = filedialog.askopenfilename()

        '''file_types = [
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
                self.preview_label.configure(image=img, text="Video file selected", compound="top", wraplength=480)'''

    def send_file(self):
        """Send file using transmitter.py"""

        '''if not self.selected_file_path:
            tk.messagebox.showerror("Error", "Please select a file!")
            return'''
  
        try:
            def encrypt_data(data, key, iv):
                cipher = AES.new(key, AES.MODE_CBC, iv)
                return cipher.encrypt(pad(data, AES.block_size))

            def add_preamble():
                # Example binary string
                binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
                file_path = self.selected_file_path
                file_name = os.path.basename(file_path).encode()
                # file_extension = os.path.splitext(file_path)[1].encode()
                with open(file_path, 'rb') as file:
                    plaintext = file.read()
                preamble = binarypreamble * 3000
                detect_sequence = b'sts'  # Sequence to detect preamble
                end_sequence = b'end'  # Sequence to detect end of file

                # AES encryption
                key = b'Sixteen byte key'  # AES key must be either 16, 24, or 32 bytes long
                iv = b'This is an IV456'  # AES IV must be 16 bytes long
                encrypted_plaintext = encrypt_data(plaintext, key, iv)
                
                with open('src/tx.tmp', 'wb') as output_file:
                    output_file.write(preamble + detect_sequence + file_name + b'|||' + encrypted_plaintext + end_sequence + preamble)

            # Adds the preamble
            add_preamble()

            # Resolve the path to the script
            transmitter_path = os.path.abspath(os.path.join(self.path, '../Transiver/File Transiver/Transmitter.py'))
            print(transmitter_path)
            '''if not os.path.exists(transmitter_path):
                raise FileNotFoundError(f"File not found: {transmitter_path}")'''

            # Start the subprocess
            print("subprocess started")
            subprocess.Popen(['python', transmitter_path], text=True)

            '''stdout, stderr = process.communicate()

            if process.returncode == 0:
                self.after(0, self.handle_transmission_success, stdout)
            else:
                self.after(0, self.handle_transmission_error, stderr)

        except subprocess.CalledProcessError as e:
            # Handle subprocess errors
            self.after(0, self.handle_transmission_error, str(e))'''
        except Exception as e:
            # Handle other unexpected errors
            #self.after(0, self.handle_transmission_error, str(e))
            pass

    def file_decoder(self):
            global content

            def open_file(file_path):
                subprocess.run(["xdg-open", file_path])
            print("file decoder started")
            while(True):
                with open('./rx.tmp', 'rb') as file:

                    content = file.read()
                    if(len(content)>10):print('conncted')
                    time.sleep(1)

                    start= content.find(b'sts')
                    if start!= -1:
                            print('file recieving')
                            end_name= content.rfind(b'|||')
                            name=content[start+3:end_name]
                            print(name)
                            end_index = content.rfind(b'end')
                            if end_index != -1:
                                start= content.find(b'|||')
                                content = content[start+3:end_index]
                                os.environ['RECEIVE_FILE']=name.decode()
                                path='./'+name.decode()
                                with open(path,'wb') as output:
                                    output.write(content)
                                    with open('./rx.tmp','wb') as output:pass
                                open_file(path)

    

if __name__ == "__main__":
    app = TransmitterApp()
    app.mainloop()
