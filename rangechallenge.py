#!/usr/bin/python3
"""Range challenge - practive using range()
    print all 99 lines of the song 99 Bottles of Beer on 
    the wall"""

def main():
    """runtime"""

    num_of_bottles = int(input("How many bottles of beer you want? "))

    print("Counting down from {num_of_bottles}")
    
    # loop in reversed to countdown
    for bottle in reversed(range(num_of_bottles)):
        print(f"{bottle} bottles of beer on the wall!\n{bottle} bottles of beer on the wall! {bottle} bottles of beer!  You take one down, pass it around!")

if __name__ == "__main__":
    main()
