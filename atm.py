originalPin = 4545
bal = 10000

pin = int(input("Enter the pin: "))
count = 1


def menu():
    print("""
    1. Account Info
    2. Check Balance
    3. Change pin
    4. Withdrawal
    5. Deposit""")


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
    