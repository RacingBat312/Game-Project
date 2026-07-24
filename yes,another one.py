from time import sleep
import textwrap
import string
import os

print("Keep my direction and soon I'll be turned to gold")
sleep(6)
print("I'm a king without a throne")
sleep(1.5)
print("A heart without a home")
sleep(1.5)
print("Just cards I've been dealt in life, uh")
sleep(2.6)
print("I walk the road alone")
sleep(1.5)
print("But my hope will never die")
sleep(3.5)

ascii_img = textwrap.dedent(r'''
          ⢀⣀⣤⣴⣶⣶⣶⣿⣿⣿⣷⢶⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠟⠉⠁⠀⠀⠀⠉⣍⣿⡿⠛⠓⠀⠉⠳⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⣀⣀⣀⠀⠹⣦⡀⠀⠀⠀⠀
⠀⠀⠛⣛⡿⠿⠶⢶⣦⣄⠀⠀⠀⠀⣿⣿⠟⣡⠞⠋⢁⡈⠻⣦⣿⣿⡄⠀⠀⠀
⠀⢠⣾⠃⠀⠀⢀⣀⣙⣏⠀⠀⠀⠀⣿⡟⣰⠋⠀⠀⠀⠷⣤⡼⢻⣿⣇⠀⠀⠀
⠀⣼⠃⠀⢠⠞⠉⠀⠀⠉⢻⣦⠀⠀⠉⠁⢣⡀⠀⠀⠀⠀⠀⠀⠀⣧⠹⣦⠀⠀
⢠⡟⠀⠀⠎⣙⣷⠀⠀⠀⠀⢉⡇⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⢀⡚ ⠀⢻⣧⠀
⢸⠇⠀⠀⣿⠉⠁⠀⠀⠀⢠⠞⣠⠞⣍⠉⣩⣉⢻⠿⣓⡒⠒⠒⠋⠀⠈⢿⡇
⢸⠀⠀⠀⠘⢦⡀⠀⢀⡴⠋⡴⣇⠀⢹⠲⠧⠉⠁⠀⠀⠉⠛⠛⠳⡀⠀⠀⢸⡇
⣾⠀⠀⠀⠀⠀⠀⠈⠉⠀⢰⣇⡽⠓⠚⠀⠀⠀⠀⠀⠀⠀⠀    ⠱⡄   ⡇
⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃ ⠀⠀⠀⠀⣀⣀⣠⠞⠉⢳⡀⢀⣀⡀⢱⠀⠀⡇
⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀ ⠀⠀⢀⡾⠀⠀⢀⣀⡀⡞⠉⡏⠀⠉⣸⠀⠀⣇
⠘⣿⡄⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠈⣁⣀⢰⡏⠀⢙⡵⠒⠛⠒⠋⠁⠀⠀⣹
⠀⠘⣧⠀⠀⠀⠀⠀⢀⠎⢀⣠⡀⢠⠞⠀⠘⢛⠱⠒⠁⠀⠀⠀⠀⠀⠀⠀⣰⡿
⠀⠀⢸⠳⣄⠀⠀⠀⠸⢦⣯⣀⣙⣋⣠⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀
⠀⠀⠘⢆⠈⠛⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀''')

print(ascii_img)

sleep(4.75)
print("But my hope will never die")
sleep(1.75)

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