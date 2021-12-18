import requests as req
import json
import pprint as p
import random
import html
url = "https://opentdb.com/api.php?amount=1"
score_correct = 0
score_incorrect = 0
endgame = ""
while endgame != "quit":
    r = req.get(url)
    if(r.status_code != 200):
        endgame = input("sorry, some sort of problem has occured, enter to try again, type 'quit' to exit")
    else:
        valid_answer = False
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print(html.unescape(question),"\n")
        for answer in answers:
            print(str(answer_number), "->", html.unescape(answer),"\n")
            answer_number = answer_number+1
        while valid_answer == False:
            user_answer = input("\n answer the question")
            try:
                user_answer = int(user_answer)
                if (user_answer > len(answers) or user_answer <=0):
                    print("invalid answer")
                else:
                    valid_answer = True
            except:
                print("invalid answer, use only numeric value")
        user_answer = answers[int(user_answer)-1]
        if(user_answer == correct_answer):
            print("congratulations, your answer is correct")
            score_correct = score_correct+1
        else:
            print("oops! your answer is incorrect, the correct answer is: ", correct_answer)
            score_incorrect = score_incorrect+1
            
        print("your score is: ")
        print("correct answer: ", str(score_correct))
        print("incorrect answer: ", str(score_incorrect))
        
        endgame = input("\n press enter to continue or type 'quit' to exit: ")
        print("\n")        
print("\nthank you for playing")