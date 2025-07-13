income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
projected_savings = int(savings * 12 * 1.05)
print("Your monthly savings are $" + str(savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")