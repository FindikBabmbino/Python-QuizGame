def StartGame():

    answers=[["A.19","B.19.5","C.21"],
             ["A.C++","B.Python","C.C#"],
             ["A.Purple","B.Black","C.Red"]]

    questions={
  "What is 9+10": "A",
  "What programming language is this written in": "B",
  "What is my favorite favorite color": "C"
}
    player_guesses = []
    question_num=0

    for i in questions:
        print("#----------")
        print(i)
        for k in answers[question_num]:
            print(k,end=" ")
        print("\n")
        guess=input("ENTER A,B, OR C: ").upper()
        SeeIfCorrect(questions[i],guess)
        player_guesses.append(guess)
        question_num+=1

    ShowScore(questions,player_guesses)

def SeeIfCorrect(answer,guess):
    if guess==answer:
        print("CORRECT")
        return 0
    else:
        print("FALSE")
        return 0

def ShowScore(answers,guesses):
    print("#---------")

    print("Correct answers: ")
    for i in answers.values():
        print(i,end=" ")

    print("\n")

    print("Your answers: ")
    for i in guesses:
        print(i,end=" ")