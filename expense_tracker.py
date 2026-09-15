expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Save Expenses")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([name, amount])
        print("Expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses")
        else:
            for expense in expenses:
                print(expense[0], "-", expense[1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("Total expenses:", total)

    elif choice == "4":
        file = open("expenses.txt", "w")

        for expense in expenses:
            file.write(expense[0] + " - " + str(expense[1]) + "\n")

        file.close()
        print("Expenses saved!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")