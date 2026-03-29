while True:
    print("\n1. Check Balance")
    print("2. View Offers")
    print("3. Special Recharge")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Your balance is Rs. 500")
    elif choice == 2:
        print("You have exciting offers!")
    elif choice == 3:
        print("Special recharge activated")
    elif choice == 0:
        break
    else:
        print("Invalid choice")