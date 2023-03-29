#quizz basic beginner project

print("\n____________________Welcome to Quizz______________________")

user = input("Do u wanna play? :").lower()
print("\n")
correct_score = 0
wrong_score = 0
if user != 'yes':
    print("Bye!")
    quit()

elif user == 'yes':
    questions = {"q1": "What does the URL stand for?",
                 "q2": "What does the HTML stand for?",
                 "q3": "What does the HTTP stand for?",
                 "q4": "What does the PDF stand for?",
                 "q5": "What does the SSD stand for?",
                 "q6": "What does the LAN stand for?",
                 "q7": "What does the CPU stand for?"
                 }

    answers =   {"a1": "uniform resource locator",
                 "a2": "hypertext markup language",
                 "a3": "hypertext transfer protocol",
                 "a4": "portable document format",
                 "a5": "solid state drive",
                 "a6": "local area network",
                 "a7": "central processing unit"
                 }

    for question in questions:
        answer = input(questions[question] + " ").lower()
        if answer == answers[question.replace("q", "a")]:
            correct_score += 1
        elif answer != answers[question.replace("q", "a")]:
            wrong_score +=1

    if correct_score == 7:
        message = "Excellent!👍"
    elif wrong_score == 7:
        message = "Poor!👎"
    elif correct_score >= 4:
        message = "Good!"
print("____________________________")
print("\nCorrect: ", correct_score)
print("Wrong: ", wrong_score)
print(message)
print("____________________________")


