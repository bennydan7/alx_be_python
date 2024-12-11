user_income = int(input("Enter your monthly income:"))
user_monthly_expenses = int(input("Enter your monthly expenses:"))


# Calculate the user's monthly savings
user_monthly_savings = user_income - user_monthly_expenses

projected_savings = user_monthly_savings * 12 + (user_monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${user_monthly_savings}.")
print(f"Projected savings after one year, with interest, is: {projected_savings}.")