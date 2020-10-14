"""
Assume a file containing a series of integers is named numbers.txt and exists
on the computer's disk. Write a program that calculates the average of all the 
numbers stored in the file.
"""


def main():
    filename = input("Enter the file you want to average: ")
    print(average_of_file(filename))


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


def average_of_file(filepath):
    sum = sum_of_file(filepath)
    fn = open(filepath, 'r')
    avg = 0
    count = 0
    line = fn.readline()

    while line != '':
        count += 1
        line = fn.readline()

    fn.close()

    avg = sum / count

    return avg


main()
