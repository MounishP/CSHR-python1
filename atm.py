# Check for the pin for three times( if its wrong)
# Menu
# Account details
originalPin = 4545
bal = 10000

pin = int(input("Enter the pin: "))
count = 1


def askMainMenu():
    print("""
    Back to (1)Main Menu or (2)exit
    """)
    choice = int(input("Enter the choice: "))
    if choice == 1:
        menu()
    else:
        exit()


def accountInfo():
    print("""
    Account Name: Python Course
    Account Number: 1234567890
    Branch: Chennai
    Bank: CSHR
    IFSC Code: CSHR997217
    """)
    askMainMenu()


def checkBalance():
    print("Available Balance: " + str(bal))
    askMainMenu()


def changePin():
    print("change pin")


def withdrawal():
    global bal
    amount = int(input("Enter the amount: "))
    # check for sufficient balance
    if amount > bal:
        print("Insufficient Balance")
        exit()

    print("Amount withdrawn")
    #update bal
    bal = bal - amount
    #show bal after update
    print("Available Balance: " + str(bal))
    #ask main menu
    askMainMenu()


def deposit():
    print("deposit")


def menu():
    print("""
    1. Account Info
    2. Check Balance
    3. Change pin
    4. Withdrawal
    5. Deposit""")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        accountInfo()
    elif choice == 2:
        checkBalance()
    elif choice == 3:
        changePin()
    elif choice == 4:
        withdrawal()
    elif choice == 5:
        deposit()
    else:
        exit()


while count < 3:
    if pin == originalPin:
        print("Account logged")
        menu()
        break
    else:
        print("Re-enter the pin")
        pin = int(input("Enter the pin: "))
        count = count + 1
else:
    print("Account blocked! Contact branch.")
