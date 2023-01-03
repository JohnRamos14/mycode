#!/usr/bin/env python3

import datetime

def main():

    user_input = input("Please enter username: ")

    now = datetime.datetime.now()

    day_of_week = now.strftime("%A")


    print(f"Hello,{user_input}! Happy {day_of_week}!")
main()

    
