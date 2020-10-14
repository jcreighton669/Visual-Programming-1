"""
Assume a file containing a series of names (as strings) is named names.txt and 
exists on the computer's disk. Write a program that displays the number of 
names that are stored in the file.
(Hint: Open the file path and read every string stored in it. Use a variable to keep count of the number of ites that are read from the file. )
"""


def main():
    filename = input("Enter the file you want read: ")
    print(count_names(filename))


def count_names(filepath):
    fn = open(filepath, 'r')
    linecount = 0
    line = fn.readline()
    while line != '':
        linecount += 1
        line = fn.readline()

    fn.close()

    return linecount


main()
