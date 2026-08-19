# Quiz Application	Show questions, accept answers, calculate score, and display results.

import os
import json

questions = [
    {
        "question": "Which language is used for AI/ML?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
        "answer": "O(log n)"
    }
]

right_ans = 0
wrong_ans = 0


def load_question():
    global questions
    if os.path.exists("question.json"):
        with open("question.json","r") as file:
            questions = json.load(file)

    else:
        save_question() 



def save_question():
    with open ("question.json","w") as file:
        json.dump(questions ,file, indent=4)

def add_question(question,options,answer):
    questions.append(
        {"question" : question,
         "options" : options,
         "answer" : answer}
    )

    print("Question added..")
    save_question()


def choose_question():
    global right_ans
    global wrong_ans

    print("\n","="*30)
    print("QUIZ COMPETITION".center(30))
    print("","="*30,"\n")

    for i in range(len(questions)):
        print(f"Q{i+1}. {questions[i]['question']}")
        for j in range(len(questions[i]['options'])):
            print(f"{j+1}. {questions[i]['options'][j]}")
        while True:    
            try:
                n = int(input("Enter the option here.: "))

                if n <= n <= len(questions[i]["options"]):
                    selected_answer = questions[i]["options"][n-1]
                    if selected_answer == questions[i]["answer"]:
                        print("Correct answer")
                        right_ans += 1
                    else:
                        print("Wrong answer. correct option is",questions[i]["answer"])
                        wrong_ans += 1

                    break    
                else:
                    print("please choose option from 1 to 4")
                

            except ValueError:
                print("Please enter the valid number.")  


    print("\n====== QUIZ COMPLETE ======")
    print(f"\nCorrect answer : {right_ans}")
    print(f"Wrong Answer   : {wrong_ans}")
    print(f"Total quetion  : {len(questions)}")   
    print(f"Final score is : {(right_ans/(len(questions))*100)}%\n")               


load_question()

while True:
    print("1. To Start Quiz...")
    print("2. to Add Question")
    print("3. To Exit")

    try:
       choice = int(input("Enter your choice from (1 to 3) here .: "))

       if choice == 1:
           choose_question()

       elif choice == 2:
           n = input("Enter the Question here.: ")
           m = (input("Enter the option here.: ").split())
           o = input("Enter the answer here .: ")
           add_question(n,m,o)  

       elif choice == 3:
           print("==== Thankyou ====")    
           break
       else:
           print("Choose the option only from (1 t 3)")

    except ValueError:
        print("please enter the valid option..")       
