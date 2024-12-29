from customtkinter import *
from PIL import Image
import tkinter as tk
import subprocess
import sys

class HomeApp(CTk):
    def __init__(self):
        super().__init__()
        self.path=os.path.dirname(os.path.abspath(__file__))
        self.geometry("700x560")
        self.resizable(0, 0)
        self.title("StarLink")  # Changed window title to "Home"

        # Logo ico Image
        try:
            # Load the icon
            icon_path = self.path + r"logo.ico"
            try:
                self.iconbitmap(icon_path)  # Use for .ico files
            except tk.TclError:
                pass
        except Exception as e:
            print(f"Error setting icon: {e}")
        
        # Initialize UI elements
        self.create_left_side_background()
        self.create_right_side_frame()

    def create_left_side_background(self):
        # Load and set the left-side background image
        background_img = Image.open("User interface/src/background_img.jpg")
        side_img = CTkImage(dark_image=background_img, light_image=background_img, size=(350, 560))
        CTkLabel(master=self, text="", image=side_img).pack(side="left")

    def create_right_side_frame(self):
        # Create the right-side frame with the specified background color
        frame = CTkFrame(master=self, width=300, height=480, fg_color="#FBE4D8")  # Right-side background color
        frame.pack_propagate(0)
        frame.pack(side="right", fill="both", expand=True)

        # Add the "Starlink" title
        CTkLabel(
            master=frame,
            text="\nStarlink",
            text_color="#522B5B",
            font=("Times New Roman Bold", 50),  # Bold and outstanding font
        ).pack(pady=(20, 10), anchor="center")  # Adjusted padding

        # Subtext under Starlink
        CTkLabel(
            master=frame, 
            text="Connect. Share. Achieve.", 
            text_color="#522B5B", 
            font=("Arial", 20), 
            anchor="center"
        ).pack(pady=(0, 40))  # Increased gap after subtext

        # Title above buttons
        CTkLabel(
            master=frame, 
            text="\n\n\nChoose an Action", 
            text_color="#854F6C", 
            font=("Arial Bold", 16), 
            anchor="center"
        ).pack(pady=(0, 15))  # Reduced gap before buttons

        # Create the buttons
        self.create_buttons(frame)

    def create_buttons(self, frame):
        # Add the "Send" button
        send_button = self.create_button(
            master=frame,
            text="Send",
            command=self.go_to_send
        )
        send_button.pack(pady=(10, 10), anchor="center")  # Reduced gap before and after buttons

        # Add the "Receive" button
        receive_button = self.create_button(
            master=frame,
            text="Receive",
            command=self.go_to_receive
        )
        receive_button.pack(pady=(0, 10), anchor="center")  # Reduced gap between buttons

        # Add the "Stream" button
        receive_button = self.create_button(
            master=frame,
            text="Stream",
            command=self.go_to_stream
        )
        receive_button.pack(pady=(0, 10), anchor="center")  # Reduced gap between buttons

    def create_button(self, master, text, command):
        button = CTkButton(
            master=master,
            text=text,
            fg_color="#854F6C",  # Button color
            hover_color="#522B5B",  # Hover color
            text_color="#190019",  # Text color
            font=("Arial Bold", 20),  # Button font
            width=180,
            height=40,
            command=command
        )
        button.bind("<Enter>", lambda e: self.on_hover(button, "#522B5B", "#FBE4D8"))  # Hover effect
        button.bind("<Leave>", lambda e: self.on_leave(button, "#854F6C", "#190019"))  # Leave effect
        return button

    def on_hover(self, button, hover_color, text_color):
        button.configure(fg_color=hover_color, text_color=text_color)

    def on_leave(self, button, original_color, text_color):
        button.configure(fg_color=original_color, text_color=text_color)

    def go_to_send(self):
        self.destroy()  # Close the current window
        subprocess.run([sys.executable, "User interface/transmitterUIDummy.py"])  # Adjust the path to your home.py file

    def go_to_receive(self):
        self.destroy()  # Close the current window
        subprocess.run([sys.executable, "User interface/receiverUIDummy.py"])  # Adjust the path to your home.py file

    def go_to_stream(self):
        self.destroy()  # Close the current window
        subprocess.run([sys.executable, "User interface/stream.py"])  # Adjust the path to your home.py file

# Run the app
if __name__ == "__main__":
    app = HomeApp()
    app.mainloop()
