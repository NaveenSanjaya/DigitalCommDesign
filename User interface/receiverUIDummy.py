from customtkinter import *
from PIL import Image
import time
import subprocess
import sys


# Initialize the app window
app = CTk()
app.geometry("600x480")
app.resizable(0, 0)
app.title("Receiver")  # Changed window title to "Receiver"

#left side bar
sidebar_frame = CTkFrame(master=app, fg_color="#522B5B",  width=150, height=480, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

back_img_data = Image.open("User interface/back.png")
back_img = CTkImage(dark_image=back_img_data, light_image=back_img_data)

def go_back_to_home():
    app.destroy()  # Close the current window
    subprocess.run([sys.executable, "User interface/home.py"])  # Adjust the path to your home.py file

back_button = CTkButton(
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
antenna_img = CTkImage(dark_image=antenna_img_data, light_image=antenna_img_data, size=(100, 100))
CTkLabel(master=sidebar_frame, text="", image=antenna_img).pack(pady=(120, 0), anchor="center")

# Create the right-side frame with the specified background color
frame = CTkFrame(master=app, width=500, height=480, fg_color="white")  # Right-side background color
frame.pack_propagate(0)
frame.pack(side="right", fill="both", expand=True)

#Top box
top_box = CTkFrame(master=frame, width=400, height=100, fg_color="#FFFFFF")
top_box.pack(anchor="n", fill="x",  padx=27, pady=(10, 0))

CTkLabel(
    master=top_box, 
    text="\n\nYou can receive", 
    text_color="#522B5B", 
    font=("Arial", 16), 
    anchor="center"
).pack(pady=(0, 10))

text_circle = CTkFrame(master=top_box, fg_color="#DFB6B2", width=50, height=50, corner_radius=100)
text_circle.pack(side="left", padx=12)

text_img_data = Image.open("User interface/text.png")
text_img = CTkImage(light_image=text_img_data, dark_image=text_img_data, size=(50, 50))

CTkLabel(master=text_circle, image=text_img, text="").grid(row=0, column=0, padx=10, pady=10)

image_circle = CTkFrame(master=top_box, fg_color="#DFB6B2", width=50, height=50, corner_radius=100)
image_circle.pack(side="left", padx=12)

img_data = Image.open("User interface/image.png")
img = CTkImage(light_image=img_data, dark_image=img_data, size=(50, 50))

CTkLabel(master=image_circle, image=img, text="").grid(row=0, column=0, padx=10, pady=10)

audio_circle = CTkFrame(master=top_box, fg_color="#DFB6B2", width=50, height=50, corner_radius=100)
audio_circle.pack(side="left", padx=12)

audio_img_data = Image.open("User interface/audio.png")
audio_img = CTkImage(light_image=audio_img_data, dark_image=audio_img_data, size=(50, 50))

CTkLabel(master=audio_circle, image=audio_img, text="").grid(row=0, column=0, padx=10, pady=10)

video_circle = CTkFrame(master=top_box, fg_color="#DFB6B2", width=50, height=50, corner_radius=100)
video_circle.pack(side="left", padx=12)

video_img_data = Image.open("User interface/video.png")
video_img = CTkImage(light_image=video_img_data, dark_image=video_img_data, size=(50, 50))

CTkLabel(master=video_circle, image=video_img, text="").grid(row=0, column=0, padx=10, pady=10)

CTkLabel(
    master=frame, 
    text="Text               Image             Audio              Video   ", 
    text_color="#522B5B", 
    font=("Arial", 14), 
    anchor="center"
).pack(pady=(0, 0))

CTkLabel(
    master=frame, 
    text="\n\n\nClick the button below to receive", 
    text_color="#522B5B", 
    font=("Arial", 16), 
    anchor="center"
).pack(pady=(0, 0))


# Create a custom hover behavior for buttons
def on_hover(button, hover_color, text_color):
    button.configure(fg_color=hover_color, text_color=text_color)

def on_leave(button, original_color, text_color):
    button.configure(fg_color=original_color, text_color=text_color)

# Functionality for the "Receive" button
def start_receiving():
    receive_button.configure(state="disabled", text="Receiving...")
    for i in range(101):
        progress_bar.set(i / 100)  # Update progress bar
        status_label.configure(text=f"Receiving... {i}%")
        app.update()  # Refresh the UI
        time.sleep(0.03)  # Simulate receiving delay
    receive_button.configure(state="normal", text="Receive")
    status_label.configure(text="File received successfully!\n\nFile name: received_file.txt")

# Add the "Receive" button

receive_img_data = Image.open("User interface/receive_icon.png")
receive_img = CTkImage(dark_image=receive_img_data, light_image=receive_img_data)

receive_button = CTkButton(
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
receive_button.bind("<Enter>", lambda e: on_hover(receive_button, "#522B5B", "#FBE4D8"))  # Hover effect
receive_button.bind("<Leave>", lambda e: on_leave(receive_button, "#854F6C", "#190019"))  # Leave effect

# Progress Bar
progress_bar = CTkProgressBar(
    master=frame,
    width=300,
    height=20,
    progress_color="#854F6C",
)
progress_bar.pack(pady=(10, 20), anchor="center")
progress_bar.set(0)  # Initial progress set to 0%

# Status Label
status_label = CTkLabel(
    master=frame,
    text="",
    text_color="#522B5B",
    font=("Arial", 14),
)
status_label.pack(pady=(10, 20), anchor="center")

# Run the app
app.mainloop()
