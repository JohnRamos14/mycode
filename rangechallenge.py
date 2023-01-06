#!/usr/bin/python3
"""Range challenge - practive using range()
    print all 99 lines of the song 99 Bottles of Beer on 
    the wall"""

def main():
    """runtime"""
    while True:
            try:
                num_of_bottles = int(input("How many bottles of beer you want? "))
                if 1 < num_of_bottles <= 100:
                    break
                else:
                    print("Can't have too much bottles!, must be between 1 and 100.")

            except ValueError:
                print("Invalid input... please enter any number between 1 and 100.")

    print("Counting down from {num_of_bottles}")
    
    # loop in reversed to countdown
    for bottle in reversed(range(num_of_bottles)):
        print(f"{bottle} bottles of beer on the wall!\n{bottle} bottles of beer on the wall! {bottle} bottles of beer!  You take one down, pass it around!")

if __name__ == "__main__":
    main()
