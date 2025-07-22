balance = 1000
pin = "1234"
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            print("Your balance:",balance)
        elif choice == "2":
            if balance <= 0:
                print("The amount is not enough")
            else:
                withdraw = float(input("Enter the amount you want:"))
                if withdraw > balance:
                    print("The amount is not enough")
                else:  
                    balance= balance - withdraw
                    print("remaining amount:",balance)
        elif choice == "3":
            deposit = float(input("Enter tyour desired deposit:"))
            balance= balance+deposit
            print("remaining amount:",balance)
        else:
            print("Exit")
            break
else:
    print("Invalid PIN")