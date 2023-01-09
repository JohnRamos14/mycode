#!/usr/env/python3
"""Code Repair challenge using built-in functions"""

def main():
    """runtime"""

    #list to print
    mylist= [1,2,3,4,5, "Python"]

    # asking input for user name
    name= input("What is your name?\n>")

    # capitalize user's name using built-in functions
    capitalized_name = name.capitalize()

    # This is what you should see when print runs-
    # Hi <name>! Welcome to Day 2 of Python Training!
    print(f"Hi {capitalized_name}! Welcome to Day {mylist[1]} of {mylist[5]} Training!")

if __name__== "__main__":
    main()
