#!/usr/bin/env python3
"""Lab 96 challenge Query Parameters
    using Open Trivia API"""

import requests
import random

URL= "https://opentdb.com/api.php?amount=3&category=21&difficulty=easy&type=multiple"

def main():

    # ask user input on playing trivia game
    
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    count = 0
    
    while count < len(data['results']):
        q = data['results'][count]
        print("\nQuestion:", q["question"])
        print(f"Enter number of correct answer")
            
        # combine all questions together
        answers = [q['correct_answer']] + q['incorrect_answers']

        # randomized the order of questions
        random.shuffle(answers)

        # use range for the list of answers to determine if user answered correctly
        for x in range(len(answers)):
            print(f"{x+1}. {answers[x]}")
        
        # asking user for an answer
        user_answer = input("Please select the correct answer: ")
        
        # checking if user got the correct answers
        if answers[int(user_answer) - 1] == q["correct_answer"]:
            print("Great Job! Your answer is correct!!")
            
            count += 1

        else:
            print("Incorrect answer! try again")

if __name__ == "__main__":
    main()

