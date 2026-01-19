balance = 0.0

while True:
    print("Welcome to the ATM!")
    
    print("1.Check Balance")    
    print("2.Deposit")    
    print("3.Withdraw")    
    print("4.Exit")

    choice = input("Please Choose an Option: ")

    if choice == "1":
        print("Your Current balance is $",balance)

    elif choice == "2":
        amount = float(input("Enter a Amount to Deposit: "))
        balance = balance + amount 
        print("Successfully deposited $",amount)

    elif choice == "3":
        amount = float(input("Enter a Amount to Withdraw: "))
        
        if amount > balance:
          print("Insufficient Balance!")
        else:
          balance = balance - amount
          print("Successfully Withdraw",amount)
          print("Remaining Balance is",balance)

    elif choice == "4":
        print("Thank You for using the ATM..")
        break

    else:
        print("Invalid Choice, Try Again")