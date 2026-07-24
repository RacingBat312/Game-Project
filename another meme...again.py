from time import sleep
import os
import string

sleep(5)
print("stinky")
sleep(0.9)
print("pussyclat")
sleep(0.9)
print("filetofish")
sleep(1.35)
print("dinidindididididididididiididididiididididididididididiidididididdiidididididididididididididiididididiid")
sleep(2)
print("bomboclat walahi")
sleep(1.5)

def print_tree(path, indent=""):
    try:
        entries = sorted(os.listdir(path))
    except (PermissionError, FileNotFoundError):
        print(indent + "[access denied]")
        return
    for entry in entries:
        full = os.path.join(path, entry)
        print(indent + entry)
        if os.path.isdir(full):
            print_tree(full, indent + "")

def show_all_drives():
    for drive in [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]:
        print(drive)
        print_tree(drive, "  ")

show_all_drives()