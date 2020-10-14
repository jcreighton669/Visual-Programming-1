mealCost = float(input("Enter the cost of the meal: "))
tipAmount = mealCost * 0.18
tax = mealCost * 0.07
totalCost = mealCost + tax + tipAmount
print("Tip Amount: $" + format(tipAmount, '.2f'))
print("Tax Amount: $" + format(tax, '.2f'))
print("Total Cost: $" + format(totalCost, '.2f'))
