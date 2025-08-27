guesses = []
score = 0
question_num = 0

answers = (("A"),("C"),("B"),("B"),("C"),)

questions = (("What is the capital of France?"),
             ("What is 5 + 7?"),
             ("Which planet is known as the Red Planet?"),
             ("What is the largest mammal on Earth?"),
             ("What is the chemical symbol for water?"),)

options = (("A) Paris", "B) Rome", "C) Madrid", "D) Berlin"),
           ("A) 10", "B) 11", "C) 12", "D) 13"),
           ("A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"),
           ("A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Orca"),
           ("A) O2", "B) CO2", "C) H2O", "D) HO2"))

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the Correct answer")

    question_num += 1
    
print("-------------------")
print("       RESULT      ")
print("-------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()

result = int(score / len(questions) * 100)

print(f"Your score is: {result}%")
    