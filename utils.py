import os
# Clear Screen - Mac, Windows, Linux
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Exit Program
def sys_exit():
    clrscr()
    print("Exiting Program...\nPress Enter to Continue...")
    input()
    raise SystemExit