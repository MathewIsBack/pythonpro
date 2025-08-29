# Concession stand program

cart = []
total = 0

menu = {
    "burger": 5.99,
    "pizza": 8.49,
    "pasta": 7.25,
    "salad": 4.50,
    "fries": 2.99,
    "soda": 1.50,
    "coffee": 2.25,
    "ice Cream": 3.75
}

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")

while True:
    food = input("Select an item (or q to quit): ").lower()

    if food == "q":
        break 
    elif menu.get(food) is not None:
        cart.append(food)


print("------- YOUR ORDER -------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is {total}")
print("--------------------------")