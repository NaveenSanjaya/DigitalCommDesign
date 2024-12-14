import customtkinter as ctk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import subprocess

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GNU Radio File Selector")
        self.root.geometry("800x600")

        self.text_file_path = ctk.StringVar()
        self.audio_file_path = ctk.StringVar()
        self.image_file_path = ctk.StringVar()
        self.video_file_path = ctk.StringVar()

        # Create frames for layout
        self.left_frame = ctk.CTkFrame(root)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(root)
        self.right_frame.pack(side="right", fill="y", padx=10, pady=10)

        # Add buttons to the right frame
        ctk.CTkButton(self.right_frame, text="Select Text File", command=self.select_text_file).pack(pady=5)
        ctk.CTkButton(self.right_frame, text="Select Audio File", command=self.select_audio_file).pack(pady=5)
        ctk.CTkButton(self.right_frame, text="Select Image File", command=self.select_image_file).pack(pady=5)
        ctk.CTkButton(self.right_frame, text="Select Video File", command=self.select_video_file).pack(pady=5)
        ctk.CTkButton(self.right_frame, text="Type and Save Text", command=self.type_and_save_text).pack(pady=5)

        # Add preview label to the left frame
        self.preview_label = ctk.CTkLabel(self.left_frame, text="")
        self.preview_label.pack(pady=10)

    def select_text_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.text_file_path.set(file_path)
            print(f"Selected Text File: {file_path}")
            with open(file_path, 'r') as file:
                content = file.read()
            self.preview_label.configure(text=content)
            subprocess.Popen(["python", "../DigitalCommDesign/text/QPSK_text_tx_rx.py", file_path])

    def select_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav *.mp3 *.ts")])
        if file_path:
            self.audio_file_path.set(file_path)
            print(f"Selected Audio File: {file_path}")
            self.preview_label.configure(text="Audio file selected: " + file_path)
            subprocess.Popen(["python", "../DigitalCommDesign/audio/QPSK_audio_tx_rx.py", file_path])

    def select_image_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.image_file_path.set(file_path)
            print(f"Selected Image File: {file_path}")
            image = Image.open(file_path)
            image = image.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.preview_label.configure(image=photo, text="")
            self.preview_label.image = photo
            subprocess.Popen(["python", "../DigitalCommDesign/image/QPSK_image_tx_rx.py", file_path])

    def select_video_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
        if file_path:
            self.video_file_path.set(file_path)
            print(f"Selected Video File: {file_path}")
            self.preview_label.configure(text="Video file selected: " + file_path)
            subprocess.Popen(["python", "../DigitalCommDesign/video/QPSK_video_tx_rx.py", file_path])

    def type_and_save_text(self):
        text = simpledialog.askstring("Input", "Type your text:")
        if text:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(text)
                self.text_file_path.set(file_path)
                self.preview_label.configure(text=text)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    root = ctk.CTk()
    app = App(root)
    root.mainloop()