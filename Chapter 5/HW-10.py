"""
One foot equals 12 inches. Write a function named feet_to_inches that accepts a
number of feet as an argument and returns the number of inches in that many 
feet. Use the function in a program that promts the user to enter a number of
feet then displays the number of inches in that many feet.
"""


def feet_to_inches(feet):
    # Convert feet to inches
    inches = feet * 12
    return str(inches)


def main():
    # Get input from the user
    user_feet = int(input('Enter the feet to convert: '))
    print(feet_to_inches(user_feet) + ' inches')


main()
