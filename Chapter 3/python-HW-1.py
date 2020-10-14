# 1)	Day of the Week Write a program that asks the user for a number in the range of 1 through 7.
# 		The program should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
# 		3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display
# 		an error message if the user enters a number that is outside the range of 1 through 7.


numDay = int(input('Enter a number for the day of the week (1-7): '))

if numDay == 1:
    print('{} = Monday'.format(numDay))
elif numDay == 2:
    print('{} = Tuesday'.format(numDay))
elif numDay == 3:
    print('{} = Wednesday'.format(numDay))
elif numDay == 4:
    print('{} = Thursday'.format(numDay))
elif numDay == 5:
    print('{} = Friday'.format(numDay))
elif numDay == 6:
    print('{} = Saturday'.format(numDay))
elif numDay == 7:
    print('{} = Sunday'.format(numDay))
else:
    print('Invalid input')
