def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

expenses = {}

while True:
    category = input("Enter expense category (or 'done' to finish): ").strip().lower()
    if category == 'done':
        break
    amount = get_amount(f"Enter amount for {category}: ")
    expenses[category] = expenses.get(category, 0) + amount  # increment the value of an existing key or add new

for category, amount in expenses.items():
    print(f"{category}: {amount:,.2f}")
    
print(f"Total expenses: {sum(expenses.values()):,.2f}")
