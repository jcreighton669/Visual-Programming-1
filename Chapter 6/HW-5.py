"""
Assume a file containing a series of integers is named numbers.txt and exists
on the computer's disk. Write a program that reads all of the numbers stored in
the file and calculates their total.
"""


def main():
    filename = input("Enter the file you want to sum: ")
    print(sum_of_file(filename))


def sum_of_file(filepath):
    fn = open(filepath, 'r')
    sum = 0
    line = fn.readline()

    while line != '':
        num = int(line)
        sum += num
        line = fn.readline()

    fn.close()

    return sum


main()
