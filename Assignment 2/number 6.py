subtotal = float(input("Enter the amount of the purchase: "))

stateTax = subtotal * 0.05
countyTax = subtotal * 0.025
totalTax = stateTax + countyTax
totalPrice = subtotal + totalTax

print("Subtotal: $" + format(subtotal, '.2f'))
print("State Sales Tax: $" + format(stateTax, '.2f'))
print("County Sales Tax: $" + format(countyTax, '.2f'))
print("Total Sales Tax: $" + format(totalTax, '.2f'))
print("Total Price: $" + format(totalPrice, '.2f'))
