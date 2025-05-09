
def check_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print("You cannot deposit negative amounts")
        return 0
    else:
       return amount

def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: "))

    if amount < 0:
        print("You cannot withdraw negative amounts")
        return 0
    elif amount > balance:
        print(f"Insufficient balance, you can withdraw not more than {balance}")
        return 0
    else:
       return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("WELCOME TO BANK")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Cancel")

        choice = input("What would you like to do, please select a number: ")

        match choice:
            case "1":
                check_balance(balance)
                check_continue = input("Would you like to continue? (y/n)")
                if check_continue == "y":
                    pass
                else:
                    is_running = False
                    print("Thank you for using Bank")

            case "2":
                balance += deposit()

            case "3":
                balance -= withdraw(balance)

            case "4":
                is_running = False
                print("Thank you for using Bank")
            case _:
                print("That is not a valid choice")


if  __name__ == "__main__":
    main()