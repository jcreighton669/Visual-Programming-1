# This programwrites three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Write the name of three philosophers
    # to the file.
    outfile.write('Justin Creighton\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()


# Call the main function.
main()
