"""
A retail company must file a monthly sales tax report listing the total sales
for the month, and the amount of state and county sales tax collected. The 
state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
Write a program that asks the user to enter the total sales for the month. From
this figure, the application should calculate and display the following: 
- The amount of county sales tax
- The amount of state sales tax
- The total sales tax (county plus state)
"""
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025


def main():
    # Get the monthly sales amount
    monthly_sales = float(input('Enter the total monthly sales: '))

    # Calculate the different tax amounts
    county_tax = float(format(monthly_sales * COUNTY_TAX_RATE, '.2f'))
    state_tax = float(format(monthly_sales * STATE_TAX_RATE, '.2f'))
    total_tax = county_tax + state_tax

    # Print the tax quantities
    print('The state tax amount is $', state_tax, sep='')
    print('The county tax amount is $', county_tax, sep='')
    print('The total sales tax amount is $', total_tax, sep='')


main()
