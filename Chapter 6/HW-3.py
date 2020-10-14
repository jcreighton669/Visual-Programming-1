"""
Write a program that asks the user for the name of a file. THe program should
display the contents of the file with each line preceded with a line number 
followed bu a colon. The line numbering should start at 1. 

ex:
1: ;dskfa;ilstengasiodnkfands;klf
2: adsflsarnwelghsdaogsaln
....
n: d;afnewfkasnsdkfghea

"""


def main():
    filename = input("Enter the file you want to print: ")
    print_lines_with_numbers(filename)


def print_lines_with_numbers(file_path):
    fn = open(file_path, 'r')
    line = fn.readline()
    linecount = 1
    while line != '':
        print(str(linecount) + ": " + line)
        linecount += 1
        line = fn.readline()

    fn.close()


main()
