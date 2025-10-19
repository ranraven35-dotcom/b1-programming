'''Business Profit Calculator
Calculates profit and margin percentage
from revenue and cost data'''

# Get revenue from user
revenue = float(input("Enter total revenue: $"))

# Get costs from user 
costs = float(input("Enter total costs: $"))

# Calculate profit
profit = revenue - costs

# Calculate profit margin percentage
margin = (profit / revenue) * 100

# Display results
print("\n--- Financial Summary ---")
print(f"Revenue: ${revenue:,.2f}")
print(f"Costs: ${costs:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {margin:.1f}%")