from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is Script 2")
    favourite_drink("soda")
    favourite_food("eggs")
    print("Goodbye")

if __name__ == '__main__':
    main()