import customtkinter as ctk
import os
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Import Image and ImageTk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time

from sympy import true

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.path=os.path.dirname(os.path.abspath(__file__))

        # Logo ico Image
        try:
            # Load the icon
            icon_path = self.path+r"logo.ico"
            try:
                self.iconbitmap(icon_path)  # Use for .ico files
            except tk.TclError:
                pass
        except Exception as e:
            print(f"Error setting icon: {e}")

        # Configure window
        self.title("StarLink")
        self.geometry("800x600")
        self.configure(fg_color="#FFFFFF")

        # Create frame for landing page
        self.landing_frame = ctk.CTkFrame(self, fg_color="white")
        self.landing_frame.pack(expand=True, fill="both")

        # Transmit Button
        transmit_button = ctk.CTkButton(
            self.landing_frame, 
            text="Send", 
            font=("Roboto", 18),
            command=self.transmittr_page,
            fg_color="#522B5B",
            hover_color="#654F6C",
            text_color="white",
            width=200,
            height=50  
        )
        transmit_button.pack(pady=(40,20))

        # Recieve Button
        recieve_button = ctk.CTkButton(
            self.landing_frame, 
            text="Receive", 
            font=("Roboto", 18),
            command=self.reciver_page,
            fg_color="#522B5B",  
            hover_color="#654F6C", 
            text_color="white",
            width=200,
            height=50  
        )
        recieve_button.pack(pady=(20,0))

        '''
        Transmtter Page (initially hidden)
        '''
        self.transmitter_frame = ctk.CTkFrame(self, fg_color="white")
        
        # Selected File Display Frame
        self.file_display_frame = ctk.CTkFrame(self.transmitter_frame, fg_color="white")
        self.file_display_frame.pack(pady=20)

        # Selected File Path Label
        self.file_path_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="No file selected", 
            text_color="black",
            font=("Roboto", 14)
            
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
            self.transmitter_frame, 
            text="", 
            text_color="green",
            font=("Roboto", 12)
        )
        self.status_label.pack(pady=10)

        # File Select Button
        select_file_button = ctk.CTkButton(
            self.transmitter_frame, 
            text="Select File", 
            font=("Roboto", 17),
            command=self.select_file,
            fg_color ="#522B5B",
            hover_color="#654F6C",
            text_color="white",
            width=200, 
            height=50
        )
        select_file_button.pack(pady =(0,0))

        # Send File Button (initially disabled)
        self.send_file_button = ctk.CTkButton(
            self.transmitter_frame, 
            text="Send File", 
            command=self.send_file,
            font=("Roboto", 15),
            fg_color="#522B5B",
            hover_color="#654F6C",
            text_color="white",
            width=150,
            height=40, 
            state="disabled",
        )
        self.send_file_button.pack(padx=(0,0))


        # Back Button
        back_button = ctk.CTkButton(
            self.transmitter_frame, 
            text="Back", 
            font=("Roboto", 15),
            command=self.show_landing_page,
            fg_color="#522B5B",  
            hover_color="#654F6C",  
            width=150, 
            height=40,
            text_color="white"
        )
        back_button.pack(padx=(0,0))

        # Initialize selected file path
        self.selected_file_path = None

        '''
        Receive Page Frame
        '''
        self.receive_frame = ctk.CTkFrame(self, fg_color="white")

        # Receive Status Frame
        self.receive_status_frame = ctk.CTkFrame(self.receive_frame, fg_color="white")
        self.receive_status_frame.pack(expand=True)

        # Receive Status Icon (Buffering/Result)
        self.receive_status_icon = ctk.CTkLabel(
            self.receive_status_frame, 
            text="🔄", 
            font=("Roboto", 142),
            text_color="gray"
        )
        self.receive_status_icon.pack(pady=(120,10))

        # Receive Status Text
        self.receive_status_text = ctk.CTkLabel(
            self.receive_status_frame, 
            text="Waiting to Receive", 
            font=("Roboto", 18),
            text_color="gray"
        )
        self.receive_status_text.pack(pady=10)

        # Received File Name Label
        self.received_file_label = ctk.CTkLabel(
            self.receive_status_frame, 
            text="", 
            font=("Roboto", 14),
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
     
    def transmittr_page(self):
        """Transition to file selection page"""
        self.landing_frame.pack_forget()
        self.transmitter_frame.pack(expand=True, fill="both")

    def reciver_page(self):
        """Transition to receive page"""
        self.landing_frame.pack_forget()
        self.receive_frame.pack(expand=True, fill="both")
        
        # Reset receive status
        self.receive_status_text.configure(text="Initializing....", text_color="gray")
        self.received_file_label.configure(text="")
        
        # Create and show loading bar
        self.progress_bar = ctk.CTkProgressBar(self.receive_status_frame, orientation="horizontal", width=400)
        self.progress_bar.pack(pady=(20, 10))
        self.progress_bar.set(0)  # Initialize progress to 0

        # Start the receive process and update the loading bar in separate threads
        threading.Thread(target=self.start_receiver, daemon=True).start()
        with open('./rx.tmp','wb') as output:pass
        threading.Thread(target=self.file_decoder,daemon=True).start()

    def select_file(self):
        """Open file dialog to select a file"""
        self.selected_file_path = filedialog.askopenfilename()
        if self.selected_file_path:
            # Update file name
            file_name = os.path.basename(self.selected_file_path)
            self.file_path_label.configure(text=file_name)
            
            # Update file size
            file_size = os.path.getsize(self.selected_file_path)
            size_str = self.format_file_size(file_size)
            self.file_size_label.configure(text=f"Size: {size_str}")
            
            # Change file icon color and enable send button
            self.send_file_button.configure(state="normal")

    def send_file(self):
            """Send file using transmitter.py"""
            if not self.selected_file_path:
                tk.messagebox.showerror("Error", "Please select a file!")
                return

            # Disable send button during transmission
            self.send_file_button.configure(state="disabled")

            # Clear any previous status message
            self.status_label.configure(text="")

            def file_encoder():
                try:
                    def encrypt_data(data, key, iv):
                        cipher = AES.new(key, AES.MODE_CBC, iv)
                        return cipher.encrypt(pad(data, AES.block_size))

                    def add_preamble():
                            # Example binary string
                        binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
                        file_path = self.selected_file_path
                        file_name = os.path.basename(file_path).encode()
                        # file_extension = os.path.splitext(file_path)[1].encode()
                        with open(file_path, 'rb') as file:
                            plaintext = file.read()
                        preamble = binarypreamble * 3000
                        detect_sequence = b'sts'  # Sequence to detect preamble
                        end_sequence = b'end'  # Sequence to detect end of file

                        # AES encryption
                        key = b'Sixteen byte key'  # AES key must be either 16, 24, or 32 bytes long
                        iv = b'This is an IV456'  # AES IV must be 16 bytes long
                        encrypted_plaintext = encrypt_data(plaintext, key, iv)
                        
                        with open('src/tx.tmp', 'wb') as output_file:
                            output_file.write(preamble + detect_sequence + file_name + b'|||' + encrypted_plaintext + end_sequence + preamble)

                    #Adds the preamble
                    add_preamble()
                    
                    # Resolve the path to the script
                    transmitter_path = os.path.abspath(os.path.join(self.path, '../Transiver/File Transiver/Transmitter.py'))

                    if not os.path.exists(transmitter_path):
                        raise FileNotFoundError(f"File not found: {transmitter_path}")

                    # Start the subprocess
                    process = subprocess.Popen(
                        ['python', transmitter_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )

                    stdout, stderr = process.communicate()

                    if process.returncode == 0:
                        self.after(0, self.handle_transmission_success, stdout)
                    else:
                        self.after(0, self.handle_transmission_error, stderr)

                except subprocess.CalledProcessError as e:
                    # Handle subprocess errors
                    self.after(0, self.handle_transmission_error, str(e))
                except Exception as e:
                    # Handle other unexpected errors
                    self.after(0, self.handle_transmission_error, str(e))

            # Run in a separate thread to prevent GUI freezing
            threading.Thread(target=file_encoder, daemon=True).start()

    def start_receiver(self):
        """Run StarLik receiver script and handle results"""
        try:
            
            # Resolve the path to the script
            reciver_path = os.path.abspath(os.path.join(self.path, '../Transiver/File Transiver/Reciver.py'))

            if not os.path.exists(reciver_path):
                raise FileNotFoundError(f"File not found: {reciver_path}")

            # Start the subprocess
            process = subprocess.Popen(
                ['python', reciver_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Capture output and errors
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                # Successful reception
                self.after(0, self.handle_receive_success, stdout.strip())
            else:
                # Reception failed
                self.after(0, self.handle_receive_error, stderr.strip())

        except Exception as e:
            # Handle any unexpected errors
            self.after(0, self.handle_receive_error, str(e))

    def file_decoder(self):
            global content

            def open_file(file_path):
                subprocess.run(["xdg-open", file_path])
            print("file decoder started")
            while(True):
                with open('./rx.tmp', 'rb') as file:

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
                                    with open('./rx.tmp','wb') as output:pass
                                open_file(path)
        
    def show_landing_page(self):
        """Return to landing page"""
        # Hide the current frame (either transmitter_frame or receive_frame)
        if self.transmitter_frame.winfo_ismapped():
            self.transmitter_frame.pack_forget()
        elif self.receive_frame.winfo_ismapped():
            self.receive_frame.pack_forget()

        # Show landing page
        self.landing_frame.pack(expand=True, fill="both")

        # Reset file selection UI elements
        self.status_label.configure(text="")
        self.send_file_button.configure(state="disabled")
        self.file_path_label.configure(text="No file selected")
        self.file_size_label.configure(text="")
        self.selected_file_path = None

        # Reset receive page UI elements
        self.receive_status_icon.configure(text="🔄", text_color="gray")
        self.receive_status_text.configure(text="Waiting to Receive", text_color="gray")
        self.received_file_label.configure(text="")

    def format_file_size(self, size_bytes):
        """Convert file size to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
  
    def handle_transmission_success(self, output):
        """Handle successful file transmission"""
        self.status_label.configure(
            text="✅ Transmission Successful", 
            text_color="green"
        )
        self.send_file_button.configure(state="normal")
        
        # Optional: Show output from StarLik.py if needed
        if output:
            tk.messagebox.showinfo("Transmission Details", output)

    def handle_transmission_error(self, error):
        """Handle transmission errors"""
        self.status_label.configure(
            text="❌ Transmission Failed", 
            text_color="red"
        )
        self.send_file_button.configure(state="normal")
        tk.messagebox.showerror("Error", error)

    def handle_receive_success(self, output):
        """Handle successful file reception"""
        # Stop progress bar updates and show success
        self.progress_bar.set(1.0)  # Complete the progress bar
        self.progress_bar.pack_forget()  # Hide the progress bar
        self.receive_status_icon.configure(text="🌳", text_color="green")
        self.receive_status_text.configure(text="File(s) Received Successfully", text_color="green")
        # Try to extract the received file name
        
    def handle_receive_error(self, error):
        """Handle reception errors"""
        self.progress_bar.pack_forget()  # Hide the progress bar
        self.receive_status_icon.configure(text="❌", text_color="red")
        self.receive_status_text.configure(text="File Reception Failed", text_color="red")
        self.received_file_label.configure(text=f"Error: {error}")
        
        # Optional: Show error message
        tk.messagebox.showerror("Receive Error", error)


if __name__ == "__main__":
    app = App()
    app.mainloop()
