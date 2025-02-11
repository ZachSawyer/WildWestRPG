from openfile import open_file
from utils import clrscr
from combat import combat
import random

def intro_text():
    clrscr()
    dialogue = open_file("dialogue.json")
    print(dialogue["intro"])
    print(dialogue["town_desc"])

def main():
    intro_text()
    combat()
    print(random.randrange(1, 5))

if __name__ == '__main__':
    main()