"""
Design a program that asks the user to enter a store's sales for each day of 
the week. The amounts should be stored in a list. Use a loop to calculate the 
total sales for the week and display the result. 
"""


def main():
    weekly_sales = []
    total_sales = 0
    for i in range(7):
        daily_sales = float(input("Enter the daily sales: "))
        weekly_sales.append(daily_sales)

    for num in weekly_sales:
        total_sales += num

    print("The total sales for the week was $", total_sales)


main()
