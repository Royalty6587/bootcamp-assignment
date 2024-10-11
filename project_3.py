income = float(input("Enter your monthly income: "))
rent = float(input("Enter your rent expenses: "))
groceries = float(input("Enter your groceries expenses: "))
utilities = float(input("Enter your utilities expenses: "))
other_expenses = float(input("Enter other expenses: "))

total_expenses = rent + groceries + utilities + other_expenses
net_savings = income - total_expenses

print(f"Total Expenses: #{total_expenses:.2f}")
print(f"Net Savings: #{net_savings:.2f}")

if net_savings > 0:
    print("You are saving money!")
elif net_savings < 0:
    print("You are overspending.")
else:
    print("You are breaking even.")
