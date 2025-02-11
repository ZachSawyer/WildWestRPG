from openfile import open_file
from utils import clrscr
from combat import combat

def intro_text():
    clrscr()
    dialogue = open_file("dialogue.json")
    print(dialogue["intro"])
    print(dialogue["town_desc"])

def main():
    intro_text()
    combat()

if __name__ == '__main__':
    main()