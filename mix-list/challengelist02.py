#!/usr/bin/python3
"""Challenge list, input,print, variables"""

# import random
import random

def main():
    """runtime"""
    
    wordbank= ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']


    # append the integer 4 to wordbank
    wordbank.append(4)

    # get the length of tlgstudents list
    length_of_students_list = len(tlgstudents)

    # input asking for a num between 1 and length of tlg students list
    num = int(input(f"Pick a number between 1 and {length_of_students_list}! ")) -1
    
    # to get the name of the tlg student picked
    # student_name = tlgstudents[num] 

    # randomize student picked
    student_name = random.choice(tlgstudents)
    print(f"{student_name}")

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent!")

if __name__ == "__main__":
    main()
