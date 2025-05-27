income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
projected_savings = savings * 12 + (savings * 12 * 0.05)

print("Your monthly saving are " + str(savings))
print("Your projected savings after one year, with interest, is: " + str(projected_savings))
