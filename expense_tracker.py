expenses = []
category_totals = {}
unique_categories = set()

print("Welcome to Personal Expense Tracker!\n")

num_expenses = 0
while True:
    try:
        num_expenses_input = input("How many expenses do you want to enter? (Enter 0 to quit): ")
        if num_expenses_input.lower() == 'q':
            print("Exiting expense entry.")
            break
        num_expenses = int(num_expenses_input)
        if num_expenses < 0:
            print("Please enter a non-negative number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number or 'q'.")

if num_expenses > 0:
    for i in range(1, num_expenses + 1):
        print(f"\nEntering Expense {i}:")
        while True:
            try:
                amount_str = input("  Amount: $")
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
        
        category = input("  Category (e.g., Food, Transport, Bills): ").strip().capitalize()
        description = input("  Description (optional): ").strip()
        
        expense_tuple = (amount, category, description if description else "No description")
        expenses.append(expense_tuple)
        
        category_totals[category] = category_totals.get(category, 0) + amount
        unique_categories.add(category)
    
    if expenses:
        all_amounts = [exp[0] for exp in expenses]
        total_spent = sum(all_amounts)
        highest_expense = max(all_amounts)
        lowest_expense = min(all_amounts)
        average_expense = total_spent / len(all_amounts)
    else:
        total_spent = 0
        highest_expense = 0
        lowest_expense = 0
        average_expense = 0
    
    print("\n" + "="*40)
    print("=== YOUR EXPENSE REPORT ===")
    print("="*40)
    
    if not expenses:
        print("No expenses recorded for this session.")
    else:
        print("\n--- All Recorded Expenses ---")
        for i, (amount, category, desc) in enumerate(expenses, 1):
            print(f"{i}. ${amount:.2f} | Category: {category} | Description: {desc}")
        
        print("\n--- Spending by Category ---")
        for category, total in sorted(category_totals.items()):
            print(f"{category}: ${total:.2f}")
        
        print("\n--- Unique Categories Tracked ---")
        print(", ".join(sorted(list(unique_categories))))
        print(f"Total unique categories: {len(unique_categories)}")
        
        print("\n--- Expense Statistics ---")
        print(f"Total Expenses: ${total_spent:.2f}")
        print(f"Highest Single Expense: ${highest_expense:.2f}")
        print(f"Lowest Single Expense: ${lowest_expense:.2f}")
        print(f"Average Expense: ${average_expense:.2f}")
    
    print("\nThank you for using the Personal Expense Tracker!")
else:
    print("\nNo expenses were entered or processed.")
