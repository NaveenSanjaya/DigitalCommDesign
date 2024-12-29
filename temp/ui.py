import customtkinter as ctk
from tkinter import filedialog, simpledialog
import os
from PIL import Image
from customtkinter import CTk, CTkLabel, CTkFrame, CTkImage
import sys
from PIL import Image, ImageTk
import subprocess
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time

class App(CTk):
    def __init__(self):
        super().__init__()
        self.path = os.path.dirname(os.path.abspath(__file__))
        
        self.geometry("600x480")
        self.resizable(0, 0)
        self.title("Home")  # Changed window title to "Home"

        # Load and set the left-side background image
        background_img = Image.open(os.path.join(self.path, "background_img.jpg"))
        side_img = CTkImage(dark_image=background_img, light_image=background_img, size=(300, 480))
        self.side_label = CTkLabel(self, text="", image=side_img)
        self.side_label.pack(side="left")

        # Create the right-side frame with the specified background color
        self.landing_frame = CTkFrame(self, width=300, height=480, fg_color="#FBE4D8")  # Right-side background color
        self.landing_frame.pack_propagate(0)
        self.landing_frame.pack(side="right", fill="both", expand=True)

        # Add the "Starlink" title
        CTkLabel(
            master=self.landing_frame,
            text="\nStarlink",
            text_color="#522B5B",
            font=("Times New Roman Bold", 50),  # Bold and outstanding font
        ).pack(pady=(20, 10), anchor="center")  # Adjusted padding

        # Subtext under Starlink
        CTkLabel(
            master=self.landing_frame, 
            text="Connect. Share. Achieve.", 
            text_color="#522B5B", 
            font=("Arial", 20), 
            anchor="center"
        ).pack(pady=(0, 40))  # Increased gap after subtext

        # Title above buttons
        CTkLabel(
            master=self.landing_frame, 
            text="\n\n\nChoose an Action", 
            text_color="#854F6C", 
            font=("Arial Bold", 16), 
            anchor="center"
        ).pack(pady=(0, 15))  # Reduced gap before buttons

        # Create a custom hover behavior for buttons
        def on_hover(button, hover_color, text_color):
            button.configure(fg_color=hover_color, text_color=text_color)

        def on_leave(button, original_color, text_color):
            button.configure(fg_color=original_color, text_color=text_color)

        # Add the "Send" button
        send_button = ctk.CTkButton(
            master=self.landing_frame,
            text="Send",
            fg_color="#854F6C",  # Button color
            hover_color="#522B5B",  # Hover color
            text_color="#190019",  # Text color
            font=("Arial Bold", 20),  # Button font
            width=180,
            height=40,
        )
        send_button.pack(pady=(10, 5), anchor="center")  # Reduced gap before and after buttons
        send_button.bind("<Enter>", lambda e: on_hover(send_button, "#522B5B", "#FBE4D8"))  # Hover effect
        send_button.bind("<Leave>", lambda e: on_leave(send_button, "#854F6C", "#190019"))  # Leave effect

        # Add the "Receive" button
        receive_button = ctk.CTkButton(
            master=self.landing_frame,
            text="Receive",
            fg_color="#854F6C",  # Button color
            hover_color="#522B5B",  # Hover color
            text_color="#190019",  # Text color
            font=("Arial Bold", 20),  # Button font
            width=180,
            height=40,
            command=self.receiver_app
        )
        receive_button.pack(pady=(0, 10), anchor="center")  # Reduced gap between buttons
        receive_button.bind("<Enter>", lambda e: on_hover(receive_button, "#522B5B", "#FBE4D8"))  # Hover effect
        receive_button.bind("<Leave>", lambda e: on_leave(receive_button, "#854F6C", "#190019"))  # Leave effect

        # Receive Page Frame
        self.receive_frame = ctk.CTkFrame(self, fg_color="white")

    def receiver_app(self):
        """Transition to receive page"""
        """Transition to receive page"""
        # Hide the landing frame
        if self.landing_frame:
            self.landing_frame.pack_forget()

        # Clear any existing frames if needed
        for widget in self.winfo_children():
            widget.destroy()


        # Create a new frame for the receiver app
        self.receive_frame = CTkFrame(master=self, width=600, height=480, fg_color="white")  # Main receiver frame
        self.receive_frame.pack_propagate(0)
        self.receive_frame.pack(fill="both", expand=True)

        self.resizable(0, 0)
        self.title("Receiver")  # Changed window title to "Receiver"

        # Left side bar
        sidebar_frame = CTkFrame(master=self.receive_frame, fg_color="#522B5B", width=150, height=480, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        back_img_data = Image.open("User interface/back.png")
        back_img = CTkImage(dark_image=back_img_data, light_image=back_img_data)

        def go_back_to_home():
            self.receive_frame.pack_forget()
            self.landing_frame.pack(fill="both", expand=True)  # Show the landing frame


        back_button = ctk.CTkButton(
            master=sidebar_frame,
            image=back_img,
            text="Back to Home",
            fg_color="transparent",
            font=("Arial Bold", 14),
            hover_color="#654F6C",
            anchor="w",
            command=go_back_to_home  # Link to the go_back_to_home function
        )
        back_button.pack(anchor="center", ipady=5, pady=(60, 0))

        antenna_img_data = Image.open("User interface/antenna.png")
        antenna_img = ctk.CTkImage(dark_image=antenna_img_data, light_image=antenna_img_data, size=(100, 100))
        ctk.CTkLabel(master=sidebar_frame, text="", image=antenna_img).pack(pady=(120, 0), anchor="center")

        # Create the right-side frame with the specified background color
        frame = ctk.CTkFrame(master=self, width=500, height=480, fg_color="white")  # Right-side background color
        frame.pack_propagate(0)
        frame.pack(side="right", fill="both", expand=True)

        # Top box
        top_box = ctk.CTkFrame(master=frame, width=400, height=100, fg_color="#FFFFFF")
        top_box.pack(anchor="n", fill="x", padx=27, pady=(10, 0))

        ctk.CTkLabel(
            master=top_box, 
            text="\n\nYou can receive", 
            text_color="#522B5B", 
            font=("Arial", 16), 
            anchor="center"
        ).pack(pady=(0, 10))

        def create_circle(master, image_path):
            circle_frame = ctk.CTkFrame(master=master, fg_color="#DFB6B2", width=50, height=50, corner_radius=100)
            circle_frame.pack(side="left", padx=12)
            img_data = Image.open(image_path)
            img = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))
            ctk.CTkLabel(master=circle_frame, image=img, text="").grid(row=0, column=0, padx=10, pady=10)

        create_circle(top_box, "User interface/text.png")
        create_circle(top_box, "User interface/image.png")
        create_circle(top_box, "User interface/audio.png")
        create_circle(top_box, "User interface/video.png")

        ctk.CTkLabel(
            master=frame, 
            text="Document           Image              Audio              Video           ", 
            text_color="#522B5B", 
            font=("Arial", 14), 
            anchor="center"
        ).pack(pady=(0, 0))

        ctk.CTkLabel(
            master=frame, 
            text="\n\n\nClick the button below to receive", 
            text_color="#522B5B", 
            font=("Arial", 16), 
            anchor="center"
        ).pack(pady=(0, 0))

        # Add the "Receive" button
        receive_img_data = Image.open("User interface/receive_icon.png")
        receive_img = ctk.CTkImage(dark_image=receive_img_data, light_image=receive_img_data)

        def start_receiving():
            receive_button.configure(state="disabled", text="Receiving...")
            for i in range(101):
                progress_bar.set(i / 100)  # Update progress bar
                status_label.configure(text=f"Receiving... {i}%")
                self.update()  # Refresh the UI
                time.sleep(0.03)  # Simulate receiving delay
            receive_button.configure(state="normal", text="Receive")
            received_file_path = "User interface/DummyImgReceived.jpeg"  # Update with actual file path
            status_label.configure(
                text="File received successfully!"
            )
            # Add clickable file name
            file_label = ctk.CTkLabel(
                master=frame,
                text=received_file_path,
                text_color="#522B5B",
                font=("Arial", 14),
                cursor="hand2"
            )
            file_label.pack(pady=(0, 0), anchor="center")
            file_label.bind("<Button-1>", lambda e: open_file(received_file_path))  # Bind click event

        def open_file(file_path):
            try:
                if os.name == "nt":  # For Windows
                    os.startfile(file_path)
                elif os.name == "posix":  # For macOS and Linux
                    subprocess.run(["xdg-open", file_path], check=True)
            except Exception as e:
                status_label.configure(text=f"Failed to open file: {e}")

        receive_button = ctk.CTkButton(
            master=frame,
            image=receive_img,
            text="Receive",
            fg_color="#854F6C",  # Button color
            hover_color="#522B5B",  # Hover color
            text_color="#190019",  # Text color
            font=("Arial Bold", 20),  # Button font
            width=180,
            height=40,
            command=start_receiving,  # Link button to the receiving functionality
        )
        receive_button.pack(pady=(10, 5), anchor="center")  # Reduced gap before and after buttons
        receive_button.bind("<Enter>", lambda e: self.on_hover(receive_button, "#522B5B", "#FBE4D8"))  # Hover effect
        receive_button.bind("<Leave>", lambda e: self.on_leave(receive_button, "#854F6C", "#190019"))  # Leave effect

        # Progress Bar
        progress_bar = ctk.CTkProgressBar(
            master=frame,
            width=300,
            height=20,
            progress_color="#854F6C",
        )
        progress_bar.pack(pady=(10, 20), anchor="center")
        progress_bar.set(0)  # Initial progress set to 0%

        # Status Label
        status_label = ctk.CTkLabel(
            master=frame,
            text="",
            text_color="#522B5B",
            font=("Arial", 14),
        )
        status_label.pack(pady=(10, 20), anchor="center")

    def on_hover(self, button, hover_color, text_color):
        button.configure(fg_color=hover_color, text_color=text_color)

    def on_leave(self, button, original_color, text_color):
        button.configure(fg_color=original_color, text_color=text_color)
    def on_hover(self, button, hover_color, text_color):
        button.configure(fg_color=hover_color, text_color=text_color)

    def on_leave(self, button, original_color, text_color):
        button.configure(fg_color=original_color, text_color=text_color)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            print(f"Selected Text File: {self.file_path}")
            with open(self.file_path, 'rb') as file:
                content = file.read().decode('utf-8', errors='ignore')
            self.preview_label.configure(text=content)
        
        threading.Thread(target=self.file_encoder, daemon=True).start()

    def file_encoder(self):
        def encrypt_data(data, key, iv):
            cipher = AES.new(key, AES.MODE_CBC, iv)
            return cipher.encrypt(pad(data, AES.block_size))

        # Example binary string
        binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
        self.file_name = os.path.basename(self.file_path).encode()
        with open(self.file_path, 'rb') as file:
            plaintext = file.read()
        preamble = binarypreamble * 3000
        detect_sequence = b'sts'  # Sequence to detect preamble
        end_sequence = b'end'  # Sequence to detect end of file

        # AES encryption
        key = b'Sixteen byte key'  # AES key must be either 16, 24, or 32 bytes long
        iv = b'This is an IV456'  # AES IV must be 16 bytes long
        encrypted_plaintext = encrypt_data(plaintext, key, iv)
        
        with open('src/tx.tmp', 'wb') as output_file:
            output_file.write(preamble + detect_sequence + self.file_name + b'|||' + encrypted_plaintext + end_sequence + preamble)

    def file_decoder(self):
        def decrypt_data(encrypted_data, key, iv):
            cipher = AES.new(key, AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(encrypted_data), AES.block_size)
        
        def open_file(file_path):
            try:
                if os.name == "nt":  # For Windows
                    os.startfile(file_path)
                elif os.name == "posix":  # For macOS and Linux
                    subprocess.run(["xdg-open", file_path], check=True)
            except Exception as e:
                self.status_label.configure(text=f"Failed to open file: {e}")

        def remove_preamble(file_path):
            detect_sequence = b'sts'
            preamble = bytes([0b10101010]) * 3000

            with open(file_path, 'rb') as file:
                content = file.read()

            start_index = content.find(detect_sequence)
            if start_index != -1:
                content = content[start_index + len(detect_sequence):]

            second_detect_index = content.find(detect_sequence)
            file_name = content[:second_detect_index]
            content = content[second_detect_index + len(detect_sequence):]

            end_index = content.rfind(detect_sequence)
            if end_index != -1:
                content = content[:end_index]

            preamble_length = len(preamble)
            while True:
                start_index = content.find(preamble)
                if start_index == -1:
                    break
                else:
                    content = content[start_index + preamble_length:]

            while True:
                end_index = content.rfind(preamble)
                if end_index == -1:
                    break
                else:
                    content = content[:end_index]

            return file_name, content

        # AES decryption
        key = b'Sixteen byte key'  # AES key must be the same as used for encryption
        iv = b'This is an IV456'  # AES IV must be the same as used for encryption

        # Remove both front and back preambles and sequence from the output.tmp file
        file_name, encrypted_content = remove_preamble('src/tx.tmp')
        decrypted_content = decrypt_data(encrypted_content, key, iv)

        # Save the decrypted content to a file
        output_file_path = f'rx src/{file_name.decode()}'
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decrypted_content)

    def receiver_app(self):
        self.geometry("600x480")
        self.resizable(0, 0)
        self.title("Receiver")  # Changed window title to "Receiver"

        # Left side bar
        sidebar_frame = ctk.CTkFrame(master=self, fg_color="#522B5B", width=150, height=480, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        back_img_data = Image.open("User interface/back.png")
        back_img = ctk.CTkImage(dark_image=back_img_data, light_image=back_img_data)

        def go_back_to_home():
            self.destroy()  # Close the current window
            subprocess.run([sys.executable, "User interface/home.py"])  # Adjust the path to your home.py file

        back_button = ctk.CTkButton(
            master=sidebar_frame,
            image=back_img,
            text="Back to Home",
            fg_color="transparent",
            font=("Arial Bold", 14),
            hover_color="#654F6C",
            anchor="w",
            command=go_back_to_home  # Link to the go_back_to_home function
        )
        back_button.pack(anchor="center", ipady=5, pady=(60, 0))

        antenna_img_data = Image.open("User interface/antenna.png")
        antenna_img = ctk.CTkImage(dark_image=antenna_img_data, light_image=antenna_img_data, size=(100, 100))
        ctk.CTkLabel(master=sidebar_frame, text="", image=antenna_img).pack(pady=(120, 0), anchor="center")

        # Create the right-side frame with the specified background color
        frame = ctk.CTkFrame(master=self, width=500, height=480, fg_color="white")  # Right-side background color
        frame.pack_propagate(0)
        frame.pack(side="right", fill="both", expand=True)

        # Top box
        top_box = ctk.CTkFrame(master=frame, width=400, height=100, fg_color="#FFFFFF")
        top_box.pack(anchor="n", fill="x", padx=27, pady=(10, 0))

        ctk.CTkLabel(
            master=top_box, 
            text="\n\nYou can receive", 
            text_color="#522B5B", 
            font=("Arial", 16), 
            anchor="center"
        ).pack(pady=(0, 10))

        def create_circle(master, image_path):
            circle_frame = ctk.CTkFrame(master=master, fg_color="#DFB6B2", width=50, height=50, corner_radius=100)
            circle_frame.pack(side="left", padx=12)
            img_data = Image.open(image_path)
            img = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))
            ctk.CTkLabel(master=circle_frame, image=img, text="").grid(row=0, column=0, padx=10, pady=10)

        create_circle(top_box, "User interface/text.png")
        create_circle(top_box, "User interface/image.png")
        create_circle(top_box, "User interface/audio.png")
        create_circle(top_box, "User interface/video.png")

        ctk.CTkLabel(
            master=frame, 
            text="Document           Image              Audio              Video           ", 
            text_color="#522B5B", 
            font=("Arial", 14), 
            anchor="center"
        ).pack(pady=(0, 0))

        ctk.CTkLabel(
            master=frame, 
            text="\n\n\nClick the button below to receive", 
            text_color="#522B5B", 
            font=("Arial", 16), 
            anchor="center"
        ).pack(pady=(0, 0))

        # Add the "Receive" button
        receive_img_data = Image.open("User interface/receive_icon.png")
        receive_img = ctk.CTkImage(dark_image=receive_img_data, light_image=receive_img_data)

        def start_receiving():
            receive_button.configure(state="disabled", text="Receiving...")
            for i in range(101):
                progress_bar.set(i / 100)  # Update progress bar
                status_label.configure(text=f"Receiving... {i}%")
                self.update()  # Refresh the UI
                time.sleep(0.03)  # Simulate receiving delay
            receive_button.configure(state="normal", text="Receive")
            received_file_path = "User interface/DummyImgReceived.jpeg"  # Update with actual file path
            status_label.configure(
                text="File received successfully!"
            )
            # Add clickable file name
            file_label = ctk.CTkLabel(
                master=frame,
                text=received_file_path,
                text_color="#522B5B",
                font=("Arial", 14),
                cursor="hand2"
            )
            file_label.pack(pady=(0, 0), anchor="center")
            file_label.bind("<Button-1>", lambda e: open_file(received_file_path))  # Bind click event

        def open_file(file_path):
            try:
                if os.name == "nt":  # For Windows
                    os.startfile(file_path)
                elif os.name == "posix":  # For macOS and Linux
                    subprocess.run(["xdg-open", file_path], check=True)
            except Exception as e:
                status_label.configure(text=f"Failed to open file: {e}")

        receive_button = ctk.CTkButton(
            master=frame,
            image=receive_img,
            text="Receive",
            fg_color="#854F6C",  # Button color
            hover_color="#522B5B",  # Hover color
            text_color="#190019",  # Text color
            font=("Arial Bold", 20),  # Button font
            width=180,
            height=40,
            command=start_receiving,  # Link button to the receiving functionality
        )
        receive_button.pack(pady=(10, 5), anchor="center")  # Reduced gap before and after buttons
        receive_button.bind("<Enter>", lambda e: self.on_hover(receive_button, "#522B5B", "#FBE4D8"))  # Hover effect
        receive_button.bind("<Leave>", lambda e: self.on_leave(receive_button, "#854F6C", "#190019"))  # Leave effect

        # Progress Bar
        progress_bar = ctk.CTkProgressBar(
            master=frame,
            width=300,
            height=20,
            progress_color="#854F6C",
        )
        progress_bar.pack(pady=(10, 20), anchor="center")
        progress_bar.set(0)  # Initial progress set to 0%

        # Status Label
        status_label = ctk.CTkLabel(
            master=frame,
            text="",
            text_color="#522B5B",
            font=("Arial", 14),
        )
        status_label.pack(pady=(10, 20), anchor="center")

    def on_hover(self, button, hover_color, text_color):
        button.configure(fg_color=hover_color, text_color=text_color)

    def on_leave(self, button, original_color, text_color):
        button.configure(fg_color=original_color, text_color=text_color)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    app = App()
    app.mainloop()