"""
Design a program that lets the user enter the total rainfall for each of 12
months into a list. The program should calculate and display the total rainfall
for the year, the average monthly rainfall, the months with the highest and
lowest amounts.
"""


def main():
    # Initialize a list to hold the rainfall values
    monthly_rainfall = []

    # Get the monthly rainfall from the user
    for i in range(12):
        rain_in_month = float(input("Enter the rainfall for the month: "))
        monthly_rainfall.append(rain_in_month)

    # Call the functions for the rainiest, driest, and total rainfall
    rainiest_month = most_rainfall_month(monthly_rainfall)
    driest_month = least_rainfall_month(monthly_rainfall)
    rainfall = total_rainfall(monthly_rainfall)

    # Print the values for the rainiest, driest, and total rainfall
    print("The rainiest month was", rainiest_month)
    print("The driest month was", driest_month)
    print("The total rain for the year was", rainfall)


# Get the month that had the most rainfall
def most_rainfall_month(arr):
    max_rainfall = max(arr)
    month = 0
    for num in arr:
        if num == max_rainfall:
            month = arr.index(max_rainfall) + 1

    get_month(month)


# Get the month that had the least rainfall
def least_rainfall_month(arr):
    min_rainfall = min(arr)
    month = 0
    for num in arr:
        if num == min_rainfall:
            month = arr.index(min_rainfall) + 1

    get_month(month)


# Get the total rainfall for the year
def total_rainfall(arr):
    rain = 0
    for num in arr:
        rain += num

    return rain


# Convert a number into its corresponding numeric value
def get_month(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"


# Call the main function
main()
