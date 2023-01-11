#!/usr/bin/env python3
"""Lab 91 Challenge: API looping
    Pokemon API"""


import requests

def main():
    """runtime"""

    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    print(pokeapi["sprites"]["front_default"])
    
    for move in pokeapi["moves"]:
        print(move["move"]["name"])
        
if __name__ == "__main__":
    main()

