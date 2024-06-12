import tkinter as tk
from tkinter import messagebox
import platform
import os

if platform.system() == "Windows":
    from camera_module_stub import capture_image
    from ignition_module_stub import start_engine, stop_engine
else:
    from camera_module import capture_image
    from ignition_module import start_engine, stop_engine

from validation_module import validate_license

class CarSecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Security System")

        self.label = tk.Label(root, text="Insert your driver’s license and press 'Start' to begin.")
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_system)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_system)
        self.stop_button.pack(pady=5)

    def start_system(self):
        capture_image()
        if validate_license():
            start_engine()
            messagebox.showinfo("Result", "Engine started!")
        else:
            stop_engine()
            messagebox.showerror("Result", "Invalid driver’s license!")

    def stop_system(self):
        stop_engine()
        messagebox.showinfo("Result", "Engine stopped.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarSecurityApp(root)
    root.mainloop()
