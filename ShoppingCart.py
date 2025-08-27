foods = []
prices = []
total = 0

while True:
    food = input("Enter food (or q to quit)")
    if food.lower() == "q":
        print("Exiting application...")
        break
    else: 
        price = float(input("Enter price of {food}: "))
        if price <= 0:
            print("Price cannot be less than or equal to zero")
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is ${total:.2f}")