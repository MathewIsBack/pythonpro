

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    while True:
        try:
            amount = float(input("Enter amount to be deposited: "))
        except ValueError:
            print("Invalid Input: Please enter a number")
            # return 0
            continue

        if amount <= 0:
            print("Invalid input: Input should be grater than 0")
            # return 0
            continue
        else:
            return amount

def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter amount to be Withdrawn: "))
        except ValueError:
            print("Invalid input: Enter a number")
            # return 0
            continue

        if amount < 0:
            print("Invalid Input")
        elif amount > balance:
            print("Insufficient funds")
        else:
            return amount
        
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*************************")
        print("     Banking Program     ")
        print("*************************")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*************************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Exiting program...")
            is_running = False
        else:
            print("")
            print("*************************")
            print("That is not a valid choice")
            print("*************************")
            print("")


if __name__ == '__main__':
    main()

