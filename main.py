#this us my first python program


#strings
first_name = "Bro"
food = "pizza"
email = "bro123@fakecom"

#Integers
age = 25
quantity = 3

#float 
price = 10.99

#boolean 
is_student = False


#price = int(price)
#print(price)
#print(type(price))

# name = input("what is your name?: ")
# age = input("how old are you: ")

# age = int(age) + 1

# print(f"Hello {name}!")
# print("Happy Birthday")
# print(f"you are {age} years old")

# Calc the area of the rectangle
# length = input("Enter the length: ")
# width = input("Enter the width: ")

# area = float(length) * float(width)

# print(f"The area is: {area}cm")

# Shopping Cart Program

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: {total}")

# while True:

    # name = input("Enter your full name: ")

    # phone_number = input("Enter a Phone Number or 'EXIT' to quit: ").strip()

    # if phone_number.lower() == "exit":
    #     print("Closing Application.... Byeee!")
    #     break


    # result = len(name)
    # result = name.find("p")
    # result = name.rfind("t")
    # result = name.capitalize()
    # result = name.upper()
    # # result = name.isdigit()
    # result = name.isalpha()
    # result = phone_number.count("-")
    # result = phone_number.replace("-", " ")


    # print(result)
# while True:
#     username = input("Please enter Username: ")

    # result = len(username)
    # result = username.find(" ")
    # result = username.isalpha()

    # if len(username) > 12:
    #     print("Username is more than 12 characters")
    # elif not username.find(" ") == -1:
    #     print("Your username can't contain spaces")
    # elif not username.isalpha():
    #     print("This username can't contain digits")
    # else:
    #     print(username)



# indexing
# credit_number = "1234-5678-9012-3456"

# # credit_number[:9]
# credit_number[::3]

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")


# Nested loops

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()

# draw a rectangle with any symbol

# rows = input("Enter the number of rows: ")
# columns = input("Enter the number of columns: ")
# symbol = input("Enter symbol you'll like to use: ")

# for x in range(int(rows)):
#     for y in range(int(columns)):
#         print(symbol, end="")
#     print()



# collections

# fruit = ["apple", "coconut", "pineapple", "orange"]

# print(fruit[1:3:2])

# groceries = [["apple","banana","orange","grape"], 
#              ["pineapple", "mango", "strawberry", "blueberry", "watermelon"],
#              ["peach", "pear", "kiwi", "coconut", "pomegranate"]]

# print(groceries[2][3])

# for collection in groceries:
#     for fruits in collection:
#         print(fruits, end=" ")
#     print()



# Dictionaries

# capitals = {"USA":"Washington D.C",
#             "India":"New Dehli",
#             "China":"Beijing",
#             "Russia":"Moscow"}

# for key in capitals.keys():
#     print(key)

# for capital in capitals.values():
#     print(capital)

# for key, value in capitals.items():
#     print(f"{key} : {value}")




# Random 
# import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# random.shuffle(cards)

# print(cards)











