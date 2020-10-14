sharesBought = 2000
boughtPrice = 40.00
soldPrice = 42.75
commissionPercent = 0.03

purchaseCost = sharesBought * boughtPrice
revenue = sharesBought * soldPrice
purchaseCommission = purchaseCost * commissionPercent
salesCommission = revenue * commissionPercent
profit = revenue - salesCommission - purchaseCost - purchaseCommission

print("Stock purchase cost: $" + format(purchaseCost, '.2f'))
print("Commision at purchase: $" + format(purchaseCommission, '.2f'))
print("Revenue for sod stock: $" + format(revenue, '.2f'))
print("Commission at stock sell: $" + format(salesCommission, '.2f'))
print("Joe made " + format(profit, '.2f') + " on this transaction.")
