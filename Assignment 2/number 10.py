CUPS_OF_SUGAR = 1.5
CUPS_OF_BUTTER = 1
CUPS_OF_FLOUR = 2.75

numCookies = int(input("Enter the number of cookies you want to make: "))

sugarNeeded = CUPS_OF_SUGAR * (numCookies / 48)
butterNeeded = CUPS_OF_BUTTER * (numCookies / 48)
flourNeeded = CUPS_OF_FLOUR * (numCookies / 48)


print("Need " + str(sugarNeeded) + " cups of sugar")
print("Need " + str(butterNeeded) + " cups of butter")
print("Need " + str(flourNeeded) + " cups of four")
