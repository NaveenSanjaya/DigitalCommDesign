import customtkinter as ctk
from customtkinter import CTkImage
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import os
import sys

'''class CTkInputDialog(ctk.CTkToplevel):
    def __init__(self, master=None, title="Input", prompt="Type your text:"):
        super().__init__(master)
        self.title(title)
        self.geometry("720x480")
        self.transient(master)
        self.prompt_label = ctk.CTkLabel(self, text=prompt, font=("Arial", 20))
        self.prompt_label.pack(pady=10)
        
        self.input_entry = ctk.CTkEntry(self, width=640, height=240)
        self.input_entry.pack(pady=20, fill="both")

        self.ok_button = ctk.CTkButton(
            self,
            text="Save",
            command=self.on_ok,
            width=100,
            height=50,
            font=("Arial", 20)
        )
        self.ok_button.pack(pady=10, padx=20, fill="both")

        self.back_button = ctk.CTkButton(
            self,
            text="Go Back",
            command=self.on_back,
            width=200,
            height=50,
            font=("Arial", 20)
        )
        self.back_button.pack(side="right", padx=10, pady=10)
        
        self.result = None

    def on_ok(self):
        self.result = self.input_entry.get()
        self.destroy()'''

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Transmitter")
        self.root.geometry("720x440")
        self.file_path = ctk.StringVar()

        # Create frames for layout
        self.left_frame = ctk.CTkFrame(root, fg_color='#854F6C')
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(root, fg_color='#FBE4D8')
        self.right_frame.pack(side="right", fill="both", padx=10, pady=10)    

        # Add button to the right frame
        ctk.CTkButton(
            self.right_frame,
            text="Select File",
            command=self.select_file,
            width=200,
            height=50,
            border_color="#000000",
            border_width=2,
            font=("Arial", 18)
        ).pack(pady=10, padx=10)

        '''ctk.CTkButton(
            self.right_frame,
            text="Type and Save Text",
            command=self.type_and_save_text,
            width=200,
            height=50,
            font=("Arial", 16)
        ).pack(pady=10)'''

        ctk.CTkButton(
            self.right_frame,
            text="Send",
            command=self.send_file,
            width=200,
            height=50,
            border_color="#000000",
            border_width=2,
            font=("Arial", 18)
        ).pack(pady=10, padx=10)

        ctk.CTkButton(
            self.right_frame,
            text="Stream",
            command=self.send_file,
            width=200,
            height=50,
            border_color="#000000",
            border_width=2,
            font=("Arial", 18)
        ).pack(pady=10, padx=10)

        ctk.CTkButton(
            self.right_frame,
            text="Back",
            command=self.go_back_to_home,
            width=200,
            height=50,
            border_color="#000000",
            border_width=2,
            font=("Arial", 18)
        ).pack(pady=10, padx=10)

        # Add preview label to the left frame
        self.preview_label = ctk.CTkLabel(self.left_frame, text="")
        self.preview_label.pack(pady=10)

        '''# Add buffer text box to the left frame
        self.buffer_text = ctk.CTkTextbox(self.left_frame, width=640, height=240)
        self.buffer_text.pack(pady=10, fill="both")'''

        # Add sending text label to the left frame
        self.sending_label = ctk.CTkLabel(self.left_frame, text="")
        self.sending_label.pack(pady=10)

    def go_back_to_home(self):
        self.root.destroy()  # Close the current window
        subprocess.run([sys.executable, "User interface/home.py"])  # Adjust the path to your home.py file

    def select_file(self):

        file_types = [
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Audio files", "*.wav *.mp3 *.ts"),
            ("Image files", "*.png *.jpg *.jpeg"),
            ("Video files", "*.mp4 *.avi")
        ]

        file_path = filedialog.askopenfilename(filetypes=file_types)
        if file_path:
            self.file_path.set(file_path)
            print(f"Selected File: {file_path}")
            self.sending_label.configure(text="")
            self.preview_label.configure(text="", image="")
            if file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    content = file.read()
                self.preview_label.configure(text=content, wraplength=480)
            elif file_path.endswith(('.wav', '.mp3')):              
                img_data = Image.open("User interface/audio.png")
                img = CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))
                self.preview_label.configure(image=img, text="Audio file selected: " + file_path, compound = "top",wraplength=480)
                
            elif file_path.endswith(('.png', '.jpg', '.jpeg')):
                image = Image.open(file_path)
                image.thumbnail((200, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.preview_label.configure(image=photo, text="")
                self.preview_label.image = photo
            elif file_path.endswith(('.mp4', '.avi', '.ts')):
                img_data = Image.open("User interface/video.png")
                img = CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))
                self.preview_label.configure(image=img, text="Video file selected: " + file_path, compound = "top",wraplength=480)
 
    def send_file(self):
        file_path = self.file_path.get()
        if file_path:
            os.environ["FILE_PATH"] = file_path
            self.sending_label.configure(text="Sending file...")
            self.progress_bar = ctk.CTkProgressBar(self.left_frame, width=480, height=20)
            self.progress_bar.pack(pady=10)
            self.progress_bar.set(0.0)
            
            def update_progress_bar():
                for i in range(101):
                    self.progress_bar.set(i / 100)
                    self.root.update_idletasks()
                    self.root.after(50)  # 50 ms delay
                self.sending_label.configure(text="File sent")
                self.progress_bar.pack_forget()  # Hide the progress bar after it is full

            self.root.after(0, update_progress_bar)
            subprocess.Popen(["python3", "../DigitalCommDesign/QPSK/QPSK_Pkt_Tx_Rx.py"])
            
    '''def type_and_save_text(self):
        dialog = CTkInputDialog(self.root)
        self.root.wait_window(dialog)
        text = dialog.result
        if text:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(text)
                self.file_path.set(file_path)
                self.preview_label.configure(text=text)
                self.buffer_text.insert("1.0", text)
                self.sending_label.configure(text="")'''

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    root = ctk.CTk()
    app = App(root)
    root.mainloop()