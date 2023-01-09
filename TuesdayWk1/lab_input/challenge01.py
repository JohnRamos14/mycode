#!/usr/bin/env python3
"""
Lab 18 Challenge. Asking for user input and printing current day of the week.
"""

from datetime import datetime

def main():
    
    # input to get  user's name
    username_input = input("Please enter username: ")

    # to get date
    now = datetime.now()

    #to get day of the week
    day_of_week = now.strftime("%A")

    # printing using f-strings
    print(f"Hello,{username_input}! Happy {day_of_week}!")

if __name__ == "__main__":
    main()

    
