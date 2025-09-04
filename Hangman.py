import random


words = ("apple","banana","coconut","orange","pineapple")


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



for line in hangman_art[6]:
    print(line)


def display_man(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    pass

if __name__ == '__main__':
    main()




