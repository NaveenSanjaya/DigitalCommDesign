from customtkinter import *
from PIL import Image
import subprocess
import sys

# Initialize the app window
app = CTk()
app.geometry("600x480")
app.resizable(0, 0)
app.title("Home")  # Changed window title to "Home"

# Load and set the left-side background image
background_img = Image.open("/home/gnuradio/Desktop/DigitalCommDesign/User interface/background_img.jpg")
side_img = CTkImage(dark_image=background_img, light_image=background_img, size=(300, 480))
CTkLabel(master=app, text="", image=side_img).pack(side="left")

# Create the right-side frame with the specified background color
frame = CTkFrame(master=app, width=300, height=480, fg_color="#FBE4D8")  # Right-side background color
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

# Create a custom hover behavior for buttons
def on_hover(button, hover_color, text_color):
    button.configure(fg_color=hover_color, text_color=text_color)

def on_leave(button, original_color, text_color):
    button.configure(fg_color=original_color, text_color=text_color)

# Add the "Send" button
send_button = CTkButton(
    master=frame,
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
def go_to_receive():
    app.destroy()  # Close the current window
    subprocess.run([sys.executable, "/home/gnuradio/Desktop/DigitalCommDesign/User interface/receiverUIDummy.py"])  # Adjust the path to your home.py file

receive_button = CTkButton(
    master=frame,
    text="Receive",
    fg_color="#854F6C",  # Button color
    hover_color="#522B5B",  # Hover color
    text_color="#190019",  # Text color
    font=("Arial Bold", 20),  # Button font
    width=180,
    height=40,
    command=go_to_receive
)
receive_button.pack(pady=(0, 10), anchor="center")  # Reduced gap between buttons
receive_button.bind("<Enter>", lambda e: on_hover(receive_button, "#522B5B", "#FBE4D8"))  # Hover effect
receive_button.bind("<Leave>", lambda e: on_leave(receive_button, "#854F6C", "#190019"))  # Leave effect

# Run the app
app.mainloop()
