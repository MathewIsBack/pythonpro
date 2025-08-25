history = []

while True:
    operator = input("Enter an Operator + - * / or 'exit' to quit: ").strip()
    # print(f"DEBUG: operator='{operator}'")

    if operator.lower() == "exit":
        print("\nExiting Calculator..... Byeeee!!")
    
        if history:
            print("\nCalculation history")
            for record in history:
                print(record)
        else:
            print("\nNo Calculations were performed.")

        break

    if operator not in ["+", "-", "*", "/"]:
        print(f"The character entered is not correct")
        continue

    num1 = float(input(f"Please enter first number: "))
    num2 = float(input(f"Please enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Division by Zero is not allowed")
            continue
        result = num1 / num2

    print("Result: ", round(result, 2))

    history.append(f"{num1} {operator} {num2} = {round(result, 2)}")