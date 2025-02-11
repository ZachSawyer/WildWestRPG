from openfile import open_file
from utils import clrscr

def intro_text():
    clrscr()
    dialogue = open_file()
    print(dialogue["intro"])
    print(dialogue["town_desc"])

def main():
    intro_text()

if __name__ == '__main__':
    main()