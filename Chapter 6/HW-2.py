"""
Write a program that asks the user for the name of a file. The program should
display only the first five lines of the file's contents. If the file contains
less than five lines, it should display the file's entire contents.
"""


# Call the file_print function from the main function.
def main():
    file_to_print = input("Enter the file address to be printed: ")
    print_file(file_to_print)


# Print either the first five lines or less of the file.
def print_file(filename):
    line_count = 0
    fn = open(filename, 'r')

    for line in fn:
        while line_count < 5 and line != '': 
            print(line)
            line_count += 1
            line = fn.readline()

    fn.close()


main()
