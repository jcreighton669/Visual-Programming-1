subtotal = 0.00
for index in range(1, 6):
    itemPrice = int(input("Enter the price of item #" + str(index) + ": "))
    subtotal += itemPrice
tax = subtotal * 0.07
total = tax + subtotal

print("Subtotal: $" + format(subtotal, '.2f'))
print("Tax: $" + format(tax, '.2f'))
print("Total: $" + format(total, '.2f'))
