import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

def get_backend_path():
    if getattr(sys, 'frozen', False):
        # If bundled with PyInstaller
        backend_path = os.path.join(sys._MEIPASS, 'backend.py')
    else:
        # If running from source
        backend_path = os.path.join(os.path.dirname(__file__), 'backend.py')
    return backend_path

backend_file = get_backend_path()

# Global variable to store the process running the Flask server
server_process = None

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_label.config(text=f"Selected folder: {folder}")
        print(f"Selected website folder: {folder}")
        return folder
    else:
        messagebox.showwarning("No Folder Selected", "Please select a folder to deploy.")
        return None

def start_server():
    global server_process
    folder = choose_folder()
    if folder:
        # Start Flask server as a new process, passing the selected folder as an argument
        server_process = subprocess.Popen(['python', backend_file, folder])
        status_label.config(text="Server Status: Running", fg="green")
        start_button.config(state="disabled")  # Disable the start button after server is running
        stop_button.config(state="normal")  # Enable the stop button
        print(f"Flask server started with folder: {folder}")
    else:
        status_label.config(text="Server Status: Not Running", fg="red")

def stop_server():
    global server_process
    if server_process:
        server_process.terminate()  # Terminates the Flask server process
        server_process = None
        status_label.config(text="Server Status: Stopped", fg="red")
        start_button.config(state="normal")  # Re-enable the start button
        stop_button.config(state="disabled")  # Disable the stop button
        print("Flask server stopped.")
    else:
        messagebox.showwarning("Server Not Running", "The server is not currently running.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Website Deployment Tool")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Header Label
header = tk.Label(root, text="Website Deployment Tool", font=("Helvetica", 16), bg="#f0f0f0")
header.pack(pady=10)

# Folder selection label
folder_label = tk.Label(root, text="No folder selected", bg="#f0f0f0")
folder_label.pack(pady=5)

# Status label
status_label = tk.Label(root, text="Server Status: Not Running", fg="red", font=("Arial", 12), bg="#f0f0f0")
status_label.pack(pady=5)

# Start and Stop Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text="Start Server", width=20, command=start_server, bg="#4CAF50", fg="white")
start_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(button_frame, text="Stop Server", width=20, command=stop_server, bg="#f44336", fg="white", state="disabled")
stop_button.grid(row=0, column=1, padx=10)

# Footer Label
footer = tk.Label(root, text="© 2024 Your Name", font=("Helvetica", 10), bg="#f0f0f0")
footer.pack(side="bottom", pady=10)

root.mainloop()
