"""
Write a program that reads the contents of the file into a list. The program 
should then ask the user to enter a charge account number. The program should 
determine whether the number is valid by searching for it in the list. If the 
number is not in the list, the program should display a message indicating the 
is invalid.
"""


def read_file():
    charge_account = []
    fn = open("charge_accounts.txt", 'r')
    for line in fn:
        charge_account.append(int(line))

    fn.close()

    return charge_account


def main():
    check_account = int(input("Enter the account number you wish to check: "))
    accounts = read_file()
