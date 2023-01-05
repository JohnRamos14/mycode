#!/usr/bin/env python3
"""Challenge dictionaries"""

def main():
    """runtime"""
    
    # asking for user input of a character they want to know about
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")
    
    # asking for user input what stats do they want to know about
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ")

    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
     "powers": "dance moves",
     "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
             }
    
    print(f"{char_name}'s {char_stat} is: {marvelchars.get(char_name).get(char_stat)}")

if __name__ == "__main__":
    main()
