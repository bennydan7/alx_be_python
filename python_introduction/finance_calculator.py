# finance_calculator.py

# Prompt the user for their monthly income
user_income = int(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
user_monthly_expenses = int(input("Enter your monthly expenses: "))

# Calculate the user's monthly savings
monthly_savings = user_income - user_monthly_expenses

# Calculate the projected annual savings with interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
