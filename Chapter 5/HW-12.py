"""
Write a function named max that accepts two integer values as arguments and 
returns the value that is the greater of the two. For example, if 7 and 12 are
passed as arguments to the function, the function should return 12. Use the 
function in a program that prompts the user to enter two integer values. The 
program should display the value that is the greater of the two. 
"""


def max(num1, num2):
    # compare the numbers to see which is bigger and return the value
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        print("The numbers are the same")
        return None


def main():
    # Get user input
    first_number = int(input('Enter your first number: '))
    second_number = int(input('Enter your second number: '))

    
    max_num = max(first_number, second_number)
    if max_num != None:
        print(max_num)


main()
