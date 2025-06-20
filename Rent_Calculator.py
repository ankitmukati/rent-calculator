print("=== Rent Calculator ===\n")

try:
    room_rent = float(input("Enter Room Rent (₹): "))
    common_expenses = float(input("Enter Common Expenses (₹): "))
    electricity_units = float(input("Enter Electricity Units used: "))
    rate_per_unit = float(input("Enter Rate per Unit (₹): "))
    persons = int(input("Enter Number of Persons: "))

    if persons <= 0:
        print("Number of persons must be at least 1.")
    else:
        electricity_bill = electricity_units * rate_per_unit
        total_expense = room_rent + common_expenses + electricity_bill
        per_person = total_expense / persons

        print("\n--- 🧾 Bill Summary ---")
        print(f"Room Rent: ₹{room_rent:.2f}")
        print(f"Common Expenses: ₹{common_expenses:.2f}")
        print(f"Electricity Bill: ₹{electricity_bill:.2f}")
        print(f"Total Expense: ₹{total_expense:.2f}")
        print(f"Each Person Should Pay: ₹{per_person:.2f}")
except ValueError:
    print("Please enter valid numbers only.")
