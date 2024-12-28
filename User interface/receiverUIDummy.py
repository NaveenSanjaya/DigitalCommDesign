from customtkinter import *
from PIL import Image
import time
import subprocess
import sys
import os
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
        self.back_img_data = Image.open("User interface/back.png")
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
        self.antenna_img_data = Image.open("User interface/antenna.png")
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
            img_data = Image.open(f"User interface/{icon}")
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
        receive_img_data = Image.open("User interface/receive_icon.png")
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

    def start_receiving(self):
        """Run StarLik receiver script and handle results"""
        try:
            
            # Resolve the path to the script
            reciver_path = os.path.abspath(os.path.join(self.path, '../Transiver/File Transiver/Reciver.py'))
            # Start the subprocess
<<<<<<< HEAD
            subprocess.Popen(['python3', reciver_path],text=True)

=======
            self.file_decoder()
            subprocess.Popen(['python', reciver_path],text=True)
            
>>>>>>> ea118739867d6a322837c13ea82c31130311aa91
            
        except Exception as e:
           pass

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

    def open_file(self, file_path):
        try:
            if os.name == "nt":
                os.startfile(file_path)
            elif os.name == "posix":
                subprocess.run(["xdg-open", file_path], check=True)
        except Exception as e:
            self.status_label.configure(text=f"Failed to open file: {e}")

    def file_decoder(self):
            global content

            def open_file(file_path):
                subprocess.run(["xdg-open", file_path])
            print("file decoder started")
            
            while(True):
                with open('./src/rx files/rx.tmp', 'rb') as file:

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
                                    with open('./src/rx files/rx.tmp','wb') as output:pass
                                    open_file(path)


def main():
    app = CTk()
    receiver_app = ReceiverApp(app)
    app.mainloop()


if __name__ == "__main__":
    main()

