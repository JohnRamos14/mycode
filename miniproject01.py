#!/usr/bin/python3
"""Mini Project - Rock, Paper, Scissors Game
    using while loop, if, elif, else, and error handling"""

import random

def main():
    """runtime"""

    # display welcome message
    print("\nRock, Paper, Scissiors Game")

    # while loop for the game
    while True:

        # error handling for invalid input
        try:            
            # asking for user input if they want to play
            print("Do you want to play? (y/n) ")
            user_response = input()
        
            # checking for valid input, if input != y or n, throw a ValueError
            if user_response.lower() != 'y':
                if user_response.lower() != 'n':
                    raise ValueError
                
                else:
                    break
       
       # inform the user of the error 
        except ValueError:
            print("Invalid input.. Please only enter y or n")
            continue
        
        # while loop so user will not come back to the start of game when they enter invalid value
        while True:
            # handling error for input rock, paper, scissors
            try:        
                # asking the user on their move
                print("\nEnter your move (rock, paper, or scissors:) ")
                user_move = input()
            
                # Make sure the user choose rock, paper, scissors only
                if user_move.lower() not in ['rock', 'paper', 'scissors']:
                    raise ValueError
                break

            # except informing user of error
            except ValueError:
                print("Invalid choice.. only enter rock, paper, or scissors")
                continue

        # randomize computer move
        computer_move = random.choice(['rock', 'paper', 'scissors'])
        print(f"The computer choose: {computer_move}")

        # determine who wins the game
        if user_move.lower() == computer_move:
            print("It's a Tie!")

        elif user_move.lower() == 'rock' and computer_move == 'scissors':
            print("You Win!")

        elif user_move.lower() == 'paper' and computer_move == 'rock':
            print("You Win!")

        elif user_move.lower() == 'scissors' and computer_move == 'paper':
            print("You Win!")

        else:
            print("The computer Wins!")

    print("Thanks for playing")



if __name__ == "__main__":
    main()
