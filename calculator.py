while True:
    operator = input("Enter an Operator + - * / or 'exit' to quit: ")

    if operator.lower() == "exit":
        print("Exiting Calculator..... Byeeee!!")
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

