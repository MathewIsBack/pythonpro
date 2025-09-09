from wordslist import words

import random


hangman_art = {
    0: ("  ",
        "  ",
        "  ",),
    1: (" 0 ",
        "  ",
        "  "),
    2: (" 0 ",
        " | ",
        "  ",),
    3: (" 0 ",
        "/| ",
        "  ",),
    4: (" 0 ",
        "/|\\",
        "  ",),
    5: (" 0 ",
        "/|\\",
        "/  ",),
    6: (" 0 ",
        "/|\\",
        "/ \\ ",)
}



# for line in hangman_art[6]:
#     print(line)


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_hint(hint)
        guess = input("Enter a Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue

        guessed_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        elif guess not in answer:
            wrong_guesses += 1
            if wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("YOU LOSE!")
                break

            display_man(wrong_guesses)

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        



if __name__ == '__main__':
    main()




