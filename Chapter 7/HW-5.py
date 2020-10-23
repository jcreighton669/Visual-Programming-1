"""
Write a program that reads the contents of the file into a list. The program 
should then ask the user to enter a charge account number. The program should 
determine whether the number is valid by searching for it in the list. If the 
number is not in the list, the program should display a message indicating the 
is invalid.
"""


# Read in the file and add the numbers to a list
def read_file():
    charge_account = []
    fn = open("charge_accounts.txt", 'r')
    for line in fn:
        charge_account.append(int(line))

    # Close the file after getting the information
    fn.close()

    # Return the list of account numbers
    return charge_account


def main():
    check_account = int(input("Enter the account number you wish to check: "))
    accounts = read_file()
    flag = False

    # Check if the input account is in the list of charge accounts.
    for i in range(len(accounts)):
        if accounts[i] == check_account:
            flag = True

    if flag == True:
        print(check_account, "is a valid account.")
    else:
        print(check_account, "is an invalid account.")


# Call the main function
main()
