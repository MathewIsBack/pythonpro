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


# Functions

# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("bro", 30)
# happy_birthday("james", 50)
# happy_birthday("sultan", 41)

# Capitlizing a full name


# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# print(create_name("naga", "larry"))


# import time 

# def count(start, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("done")

# count(0,10)


# get a phone number

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(1,234,567,89)

# print(phone_num)



# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(4, 5))


# def name(*args):
#     for arg in args:
#         print(arg, end=" ")
    
# name("dr","junir","paganini")    


# def print_address(**kwargs):
#     for key, values in kwargs.items():
#         print(f"{key} : {values}")

# print_address(
#     street = "123 fake st",
#     city = "Detroit",
#     state = "MI",
#     zip = "54321"
# )


# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()

#     # for values in kwargs.values():
#     #     print(values, end=" ")
#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     else:
#         print(f"{kwargs.get('street')}")
#         print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

# shipping_label("Dr.","Gaven","Hunt",
#                 street = "123 fake st",
#                 apt = "#78",
#                 city = "Detroit",
#                 state = "MI",
#                 zip = "54321"
#                )


# grades = {
#     "sandy": "A",
#     "squidward": "B",
#     "spongebob": "C",
#     "patrick": "D"
# }

# student = input("Enter the name of the student: ").lower()

# print(grades["Sandy"])

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")



# List Comprehension

# [Expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]

# squares = [z * z for z in range(1, 11)]

# print(squares)

# fruits = ["apple", "coconut", "banana", "pineapple"]

# fruit_chars = [fruit[0] for fruit in fruits]

# print(fruit_chars)


# numbers = [-7, -1, -2, -4, 5, 9, 6, 3]

# positive_num = [num for num in numbers if num >= 0]
# negative_num = [num for num in numbers if num < 0]
# even = [num for num in numbers if num % 2 == 0]
# odd = [num for num in numbers if num % 2 == 1]

# print(odd)


# grades = [86, 54, 67, 78, 29, 14, 43]

# passing_grades = [grade for grade in grades if grade >= 60] 

# print(passing_grades)


# def is_weekend(day):
#     match day:
#         case "sunday" | "saturday":
#             return True
#         case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
#             return False
#         case _:
#             return False
        
# print(is_weekend("saturday"))


# CREATING YOUR OWN MODULES

import module

# result = module.area(12)
# result = module.circumference(34)
# result = module.cube(3)
# result = module.square(5)

# print(result)













