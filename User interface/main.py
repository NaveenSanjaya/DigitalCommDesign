import customtkinter as ctk
import os
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Import Image and ImageTk
from Crypto.Cipher import AES
import time

from sympy import true

class TransmittingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.path=os.path.dirname(os.path.abspath(__file__))

        # Try to set icon using PIL Image
        try:
            # Load the icon
            icon_path = self.path+r"/transmitter/src/signal-tower.ico"  # Example location
            try:
                self.iconbitmap(icon_path)  # Use for .ico files
            except tk.TclError:
                pass
        except Exception as e:
            print(f"Error setting icon: {e}")

        # Configure window
        self.title("TeleLink Communications")
        self.geometry("800x600")
        self.configure(fg_color="#FFFFFF")

        # Create frame for landing page
        self.landing_frame = ctk.CTkFrame(self, fg_color="white")
        self.landing_frame.pack(expand=True, fill="both")

        try:
            image_path = self.path+r"/transmitter/src/bladeLINK.png"  # Ensure this path is correct
            title_image = Image.open(image_path)
            title_image = title_image.resize((300, 140), Image.LANCZOS)  # Resize if needed
            title_photo = ctk.CTkImage(light_image=title_image, size=(300, 140))  # Convert to CTkImage
            title_label = ctk.CTkLabel(
                self.landing_frame, 
                image=title_photo, 
                text=""
            )
            title_label.pack(pady=(120, 0))
        except Exception as e:
            print(f"Error loading title image: {e}")


        # Start Button
        transmit_button = ctk.CTkButton(
            self.landing_frame, 
            text="Send", 
            font=("Roboto", 18),
            command=self.open_file_page,
            fg_color="#2ECC71",  # Emerald
            hover_color="#27AE60",  # Green Sea
            text_color="white",
            width=200,  # Adjust the width as needed
            height=50  
        )
        transmit_button.pack(pady=(40,20))

        # Recieve Button
        recieve_button = ctk.CTkButton(
            self.landing_frame, 
            text="Receive", 
            font=("Roboto", 18),
            command=self.open_receive_page,
            fg_color="#3498DB",  # Peter River
            hover_color="#2980B9",  # Belize Hole
            text_color="white",
            width=200,
            height=50  
        )
        recieve_button.pack(pady=(20,0))

        # Logo Frame (bottom right)
        logo_frame = ctk.CTkFrame(self.landing_frame, fg_color="white")
        logo_frame.pack(side="bottom", anchor="se", padx=20, pady=20)

        # Load and display logo using PIL Image and ImageTk.PhotoImage
        try:
            image_path = self.path+r"/transmitter/src/telelink.png"
            logo_image = Image.open(image_path)  # Use PIL to open the image
            logo_image = logo_image.resize((150, 150), Image.LANCZOS)  # Resize if needed
            logo_photo = ctk.CTkImage(light_image=logo_image, size=(150, 150))  # Convert to CTkImage
            logo_label = ctk.CTkLabel(
                logo_frame, 
                image=logo_photo, 
                text=""
            )
            logo_label.photo = logo_photo  # Keep reference to avoid garbage collection
            logo_label.pack(fill="both", expand=True)
        except Exception as e:
            print(f"Error loading logo: {e}")
            logo_label = ctk.CTkLabel(
                logo_frame, 
                text="Telelink", 
                font=("Roboto", 12)
            )
            logo_label.pack()

        # File Selection Page (initially hidden)
        self.file_frame = ctk.CTkFrame(self, fg_color="white")
        
        # Selected File Display Frame
        self.file_display_frame = ctk.CTkFrame(self.file_frame, fg_color="white")
        self.file_display_frame.pack(pady=20)

        # File Icon
        self.file_icon_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="📄", 
            font=("Arial", 142),  # Increase the font size
            text_color="gray"
        )
        self.file_icon_label.pack(pady=(90,1))

        # Selected File Path Label
        self.file_path_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="No file selected", 
            text_color="black",
            font=("Arial", 14)
            
        )
        self.file_path_label.pack(pady=0)

        # File Size Label
        self.file_size_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="", 
            text_color="gray"
        )
        self.file_size_label.pack(pady=5)

        # Transmission Status Label
        self.status_label = ctk.CTkLabel(
            self.file_frame, 
            text="", 
            text_color="green",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=10)

        # File Select Button
        file_select_button = ctk.CTkButton(
            self.file_frame, 
            text="Select File", 
            font=("Roboto", 17),
            command=self.select_file,
            fg_color ="#2C3E50",
            hover_color="#34495E",
            text_color="white",
            width=200,  # Adjust the width as needed
            height=50   # Adjust the height as needed
        )
        file_select_button.pack(pady =(0,0))

        # Send File Button (initially disabled)
        self.send_file_button = ctk.CTkButton(
            self.file_frame, 
            text="Send File", 
            command=self.send_file,
            font=("Roboto", 15),
            fg_color="#2ECC71",
            hover_color="#58D68D",
            text_color="white",
            width=150,  # Adjust the width as needed
            height=40,   # Adjust the height as needed
            state="disabled",
        )
        self.send_file_button.pack(side="left", padx=(190,0))


        # Back Button
        back_button = ctk.CTkButton(
            self.file_frame, 
            text="Back", 
            font=("Roboto", 15),
            command=self.show_landing_page,
            fg_color="#FF6F61",  # Coral
            hover_color="#FF4F4F",  # Light Red
            width=150,  # Adjust the width as needed
            height=40,   # Adjust the height as needed
            text_color="white"
        )
        back_button.pack(side="right", padx=(0,190))

        # Initialize selected file path
        self.selected_file_path = None

        # Receive Page Frame
        self.receive_frame = ctk.CTkFrame(self, fg_color="white")

        # Receive Status Frame
        self.receive_status_frame = ctk.CTkFrame(self.receive_frame, fg_color="white")
        self.receive_status_frame.pack(expand=True)

        # Receive Status Icon (Buffering/Result)
        self.receive_status_icon = ctk.CTkLabel(
            self.receive_status_frame, 
            text="🔄", 
            font=("Arial", 142),
            text_color="gray"
        )
        self.receive_status_icon.pack(pady=(120,10))

        # Receive Status Text
        self.receive_status_text = ctk.CTkLabel(
            self.receive_status_frame, 
            text="Waiting to Receive", 
            font=("Arial", 18),
            text_color="gray"
        )
        self.receive_status_text.pack(pady=10)

        # Received File Name Label
        self.received_file_label = ctk.CTkLabel(
            self.receive_status_frame, 
            text="", 
            font=("Arial", 14),
            text_color="black"
        )
        self.received_file_label.pack(pady=10)

        # Back Button for Receive Page
        back_button = ctk.CTkButton(
            self.receive_frame, 
            text="Back", 
            command=self.show_landing_page,
            fg_color="#E74C3C",
            hover_color="#C0392B",
            text_color="white"
        )
        back_button.pack(side="bottom", pady=20)

    def open_receive_page(self):
        """Transition to receive page"""
        self.landing_frame.pack_forget()
        self.receive_frame.pack(expand=True, fill="both")
        
        # Reset receive status
        self.receive_status_icon.configure(text="🔄", text_color="gray")
        self.receive_status_text.configure(text="Waiting to Receive", text_color="gray")
        self.received_file_label.configure(text="")
        
        # Start receive process in a thread
        threading.Thread(target=self.start_receive_process, daemon=True).start()
        threading.Thread(target=self.file_decoder,daemon=True).start()



if __name__ == "__main__":
    app = TransmittingApp()
    app.mainloop()
