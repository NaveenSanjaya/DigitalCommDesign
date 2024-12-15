import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import subprocess

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GNU Radio File Selector")

        self.text_file_path = tk.StringVar()
        self.audio_file_path = tk.StringVar()
        self.image_file_path = tk.StringVar()
        self.video_file_path = tk.StringVar()

        tk.Button(root, text="Select Text File", command=self.select_text_file).pack(pady=5)
        tk.Button(root, text="Select Audio File", command=self.select_audio_file).pack(pady=5)
        tk.Button(root, text="Select Image File", command=self.select_image_file).pack(pady=5)
        tk.Button(root, text="Select Video File", command=self.select_video_file).pack(pady=5)
        tk.Button(root, text="Type and Save Text", command=self.type_and_save_text).pack(pady=5)

    def select_text_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.text_file_path.set(file_path)
            print(f"Selected Text File: {file_path}")
            subprocess.Popen(["python", "../DigitalCommDesign/text/QPSK_text_tx_rx.py", file_path])

    def select_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav *.mp3 *.ts")])
        if file_path:
            self.audio_file_path.set(file_path)
            print(f"Selected Audio File: {file_path}")
            subprocess.Popen(["python", "../DigitalCommDesign/text/QPSK_text_tx_rx.py", file_path])

    def select_image_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.image_file_path.set(file_path)
            print(f"Selected Image File: {file_path}")
            subprocess.Popen(["python", "../DigitalCommDesign/image/QPSK_image_tx_rx.py"])

    def select_video_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
        if file_path:
            self.video_file_path.set(file_path)
            print(f"Selected Video File: {file_path}")
            subprocess.Popen(["python", "../DigitalCommDesign/video/QPSK_video_tx_rx.py", file_path])

    def type_and_save_text(self):
        text = simpledialog.askstring("Input", "Type your text:")
        if text:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(text)
                self.text_file_path.set(file_path)
                print(f"Text saved to: {file_path}")
                subprocess.Popen(["python", "../DigitalCommDesign/text/QPSK_text_tx_rx.py", file_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    import tkinter.ttk as ttk

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)
    style.configure("TLabel", font=("Helvetica", 12), padding=10)

    root.geometry("40x300")
    root.configure(bg="#f0f0f0")

    for widget in root.winfo_children():
        widget.configure(style="TButton")

    root.mainloop()