import json
from utils import clrscr, sys_exit

# Open JSON File with Error Handling
def open_file():
    try:
        with open("dialogue.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        clrscr()
        print("File Not Found\nPress Enter to Continue...")
        input()
        sys_exit()
    except json.JSONDecodeError as e:
        clrscr()
        print(f"Error: {e}\nPress Enter to Continue...")
        input()
        sys_exit()