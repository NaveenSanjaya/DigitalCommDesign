from customtkinter import *
from PIL import Image
import time
import subprocess
import threading
import sys
import os
import platform
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

class ReceiverApp:
    def __init__(self, master):
        super().__init__()
        self.path=os.path.dirname(os.path.abspath(__file__))

        self.master = master
        self.master.geometry("700x560")
        self.master.resizable(0, 0)
        self.master.title("Receiver")

        # Sidebar frame
        self.sidebar_frame = CTkFrame(master=self.master, fg_color="#522B5B", width=150, height=480, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        # Back button
        self.back_img_data = Image.open("User interface/src/back.png")
        self.back_img = CTkImage(dark_image=self.back_img_data, light_image=self.back_img_data)
        self.back_button = CTkButton(
            master=self.sidebar_frame,
            image=self.back_img,
            text="Back to Home",
            fg_color="transparent",
            font=("Arial Bold", 14),
            hover_color="#654F6C",
            anchor="w",
            command=self.go_back_to_home
        )
        self.back_button.pack(anchor="center", ipady=5, pady=(60, 0))

        # Antenna image
        self.antenna_img_data = Image.open("User interface/src/antenna.png")
        self.antenna_img = CTkImage(dark_image=self.antenna_img_data, light_image=self.antenna_img_data, size=(100, 100))
        CTkLabel(master=self.sidebar_frame, text="", image=self.antenna_img).pack(pady=(120, 0), anchor="center")

        # Main frame
        self.frame = CTkFrame(master=self.master, width=500, height=480, fg_color="white")
        self.frame.pack_propagate(0)
        self.frame.pack(side="right", fill="both", expand=True)

        # Top Box
        self.top_box = CTkFrame(master=self.frame, width=400, height=100, fg_color="#FFFFFF")
        self.top_box.pack(anchor="n", fill="x", padx=50, pady=(10, 0))

        self.create_top_box_labels()

        # Text above the button
        self.receive_text_label = CTkLabel(
            master=self.frame,
            text="Click the button below to receive",
            text_color="#522B5B",
            font=("Arial", 16),
            anchor="center"
        )
        self.receive_text_label.pack(pady=(20, 10), anchor="center")

        # Receive button and progress bar
        self.receive_button = self.create_receive_button()
        self.progress_bar = self.create_progress_bar()

        # Status label
        self.status_label = CTkLabel(
            master=self.frame,
            text="",
            text_color="#522B5B",
            font=("Arial", 14),
        )
        self.status_label.pack(pady=(10, 20), anchor="center")

        # Add the data rate label
        self.data_rate_label = CTkLabel(
            master=self.frame,
            text="Data rate: 0.00 KB/s",
            text_color="#522B5B",
            font=("Arial", 14),
            anchor="center"
        )
        self.data_rate_label.pack(pady=(10, 20), anchor="center")

    def create_top_box_labels(self):
        CTkLabel(
            master=self.top_box,
            text="\n\nYou can receive",
            text_color="#522B5B",
            font=("Arial", 16),
            anchor="center"
        ).pack(pady=(0, 10))

        icons = [("text.png", "Document"), ("image.png", "Image"), ("audio.png", "Audio"), ("video.png", "Video")]
        
        # Create a frame to hold the images and their respective labels
        images_frame = CTkFrame(master=self.top_box, fg_color="transparent")
        images_frame.pack(anchor="n", fill="x", pady=0)

        # Create a container for each image and its label
        for icon, label in icons:
            # Frame for the image and label
            container_frame = CTkFrame(master=images_frame, fg_color="transparent")
            container_frame.pack(side="left", padx=20, pady=10, anchor="center")

            # Circle frame for the image
            circle_frame = CTkFrame(master=container_frame, fg_color="#DFB6B2", width=100, height=100, corner_radius=100)
            circle_frame.pack(fill="both", pady=(0, 10))

            # Image
            img_data = Image.open(f"User interface/src/{icon}")
            img = CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))
            CTkLabel(master=circle_frame, image=img, text="").pack(fill="both", padx=10, pady=10)  # Image inside the circle frame

            # Label below the image
            label_text = CTkLabel(
                master=container_frame,
                text=label,
                text_color="#522B5B",
                font=("Arial", 14),
                anchor="center"
            )
            label_text.pack(fill="both")

    def create_receive_button(self):
        receive_img_data = Image.open("User interface/src/receive_icon.png")
        receive_img = CTkImage(dark_image=receive_img_data, light_image=receive_img_data)

        receive_button = CTkButton(
            master=self.frame,
            image=receive_img,
            text="Receive",
            fg_color="#854F6C",
            hover_color="#522B5B",
            text_color="#190019",
            font=("Arial Bold", 20),
            width=180,
            height=40,
            command=self.start_receiving,
        )
        receive_button.pack(pady=(10, 5), anchor="center")
        receive_button.bind("<Enter>", lambda e: self.on_hover(receive_button, "#522B5B", "#FBE4D8"))
        receive_button.bind("<Leave>", lambda e: self.on_leave(receive_button, "#854F6C", "#190019"))
        return receive_button

    def create_progress_bar(self):
        progress_bar = CTkProgressBar(
            master=self.frame,
            width=300,
            height=20,
            progress_color="#854F6C",
        )
        progress_bar.pack(pady=(10, 20), anchor="center")
        progress_bar.set(0)  # Initial progress set to 0%
        return progress_bar

    def on_hover(self, button, hover_color, text_color):
        button.configure(fg_color=hover_color, text_color=text_color)

    def on_leave(self, button, original_color, text_color):
        button.configure(fg_color=original_color, text_color=text_color)

    def go_back_to_home(self):
        self.master.destroy()
        subprocess.run([sys.executable, "User interface/home.py"])

    def create_file_label(self, file_path):
        file_label = CTkLabel(
            master=self.frame,
            text=file_path,
            text_color="#522B5B",
            font=("Arial", 14),
            cursor="hand2"
        )
        file_label.pack(pady=(0, 0), anchor="center")
        file_label.bind("<Button-1>", lambda e: self.open_file(file_path))

    def calculate_data_rate(self, file_path):
        """Calculates and displays the data rate of the given file."""
        last_size = 0
        start_time = time.time()

        while True:
            try:
                current_size = os.path.getsize(file_path)
                elapsed_time = time.time() - start_time

                if elapsed_time > 0:
                    data_rate = (current_size - last_size) / elapsed_time  # Bytes per second
                    # Format data rate in KB/s for better readability
                    data_rate_kb = data_rate / 1024 * 8
                    start_time = time.time()
                    last_size = current_size

                    # Update the label text in a thread-safe way
                    self.update_data_rate_label(data_rate_kb)

                time.sleep(1)  # Check every second
            except FileNotFoundError:
                self.update_data_rate_label(0)
                time.sleep(1)

    def update_data_rate_label(self, data_rate_kb):
        """Updates the data rate label on the GUI."""
        text = f"Data rate: {data_rate_kb:.2f} Kbps" if data_rate_kb > 0 else "Waiting for data..."
        self.data_rate_label.configure(text=text)

    def start_receiving(self):
        """Starts the receiver and data rate calculation in separate threads."""
        threading.Thread(target=self.start_receiver, daemon=True).start()
        
        # Clear the temporary file
        with open('./Transiver/File Transiver/rx.tmp', 'wb') as output:
            pass

        # Start the data rate thread
        file_path = './Transiver/File Transiver/rx.tmp'
        threading.Thread(target=self.calculate_data_rate, args=(file_path,), daemon=True).start()
        
        # Start the file decoding thread
        threading.Thread(target=self.file_decoder, daemon=True).start()

        # Start progress bar thread
        threading.Thread(target=self.update_progress_bar, daemon=True).start()

        
    def update_progress_bar(self):
        """Completes the progress bar in 8 seconds."""
        duration = 8  # seconds
        steps = 100  # Number of steps to divide the progress
        step_duration = duration / steps  # Time per step

        for i in range(steps + 1):  # +1 to ensure it reaches 100%
            progress = i / steps  # Progress value (0 to 1)
            self.progress_bar.set(progress)
            time.sleep(step_duration)
            
    def data_rate_elements(self):
        """Adds GUI elements for data rate display."""
        # Add a label for showing the data rate
        self.data_rate_label = CTkLabel(
            master=self.frame,
            text="Data rate: 0.00 KB/s",
            text_color="#522B5B",
            font=("Arial", 14),
        )
        self.data_rate_label.pack(pady=(10, 20), anchor="center")

    def start_receiver(self):
        """Run StarLik receiver script and handle results"""
        try:
            
            # Resolve the path to the script
            reciver_path = os.path.abspath(os.path.join(self.path, '../Transiver/File Transiver/Reciver.py'))
            # Start the subprocess
            subprocess.Popen(['python', reciver_path],text=True)

            
        except Exception as e:
           print(e)

    def file_decoder(self):
        global content

        def open_file(file_path):
            if platform.system() == "Windows":
                print(file_path)
                os.startfile(file_path)
            else:
                subprocess.run(["xdg-open", file_path])

        print("File decoding started")

        while True:
            with open('./Transiver/File Transiver/rx.tmp', 'rb') as file:
                content = file.read()
                if len(content) > 10:
                    print('Connected')
                    time.sleep(1)

                    start = content.find(b'sts')
                    if start != -1:
                        print('File receiving')
                        end_name = content.rfind(b'|||')
                        if end_name != -1:
                            name = content[start + 3:end_name].decode()  # Decoding the file name
                            print(name)

                            end_index = content.rfind(b'end')
                            if end_index != -1:
                                start = content.find(b'|||')
                                content = content[start + 3:end_index]

                                os.environ['RECEIVE_FILE'] = name

                                # Use os.path.join for correct path concatenation
                                base_dir = './Transiver/File Transiver'
                                path = os.path.abspath(os.path.join(base_dir, name))  # Convert to absolute path

                                # Ensure the directory exists
                                os.makedirs(base_dir, exist_ok=True)

                                with open(path, 'wb') as output:
                                    output.write(content)

                                # Clear the temporary file
                                with open('./Transiver/File Transiver/rx.tmp', 'wb') as output:
                                    pass
                            
                                # Open the file
                                open_file(path)

    

def main():
    app = CTk()
    receiver_app = ReceiverApp(app)
    app.mainloop()


if __name__ == "__main__":
    main()

