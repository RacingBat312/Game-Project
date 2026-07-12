import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window


msg = "sorry bro, ts beat is ass"
detail = "session terminated"

result = messagebox.askokcancel("Error", f"{msg}\n\n{detail}", icon="error")

root.destroy()  # Close the main window after the message box is closed