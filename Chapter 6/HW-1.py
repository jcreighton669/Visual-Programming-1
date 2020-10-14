"""
Assume a file conatining a series of integers is named numbers.txt and exists
on the computers disk. Write a program that displays all the numbers in a file.
"""


def main():
    # Open the numbers.txt file for reading.
    numbers_file = open('numbers.txt', 'r')

    line = numbers_file.readline()

    while line != '':
        # Convert line to an integer.
        num = int(line)

        # format and display the number.
        print(format(num, ','))

        line = numbers_file.readline()

    # Close the file.
    numbers_file.close()


main()
