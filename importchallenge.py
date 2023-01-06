#!/usr/bin/python3
"""Module import challenge - clean up data that was 
    return in HTML format using the HTML module"""

import html

def main():
    """runtime"""

    trivia= {
             "category": "Entertainment: Film",
             "type": "multiple",
             "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
             "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
             "incorrect_answers": [
                 "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                 "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                 "&quot;Round up the usual suspects.&quot;"
                ]
          }
    
    # getting the value of question
    question = trivia["question"]
    print("\n", question)

    # getting the value of the correct_answer
    correct_ans = html.unescape(trivia["correct_answer"])
    print("\na.", correct_ans)
   
    # values if incorrect_answers
    incorrect_ans1 = html.unescape(trivia["incorrect_answers"][0])
    incorrect_ans2 = html.unescape(trivia["incorrect_answers"][1])
    incorrect_ans3 = html.unescape(trivia["incorrect_answers"][2])

    # display incorrect_answers
    print("\nb.", incorrect_ans1)
    print("\nc.", incorrect_ans2)
    print("\nd.", incorrect_ans3)

    while True:
    
        # asking user input for correct answer
        user_ans = input("\nWhich one of the follwing is the correct answer? a, b, c, or d\n")
            
        #checking if user have the correct answer
        if user_ans == 'a'.lower():
            print("Great job!")
            break
        else:
            print("Sorry... Wrong answer!")

if __name__ == "__main__":
    main()



            
