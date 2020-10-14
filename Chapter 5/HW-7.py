"""
There are three seating categories at a stadium. Class A seats cost $20, Class
B seats cost $15, and Class C seats cost $10. Write a program that asks how 
many tickets for each class of seats were sold, then displays the amount of 
income generated from ticket sales.
"""
CLASS_A_SEAT = 20
CLASS_B_SEAT = 15
CLASS_C_SEAT = 10


def main():
    num_a_seats = int(input('Enter the number of Class A seats to purchase: '))
    num_b_seats = int(input('Enter the number of Class B seats to purchase: '))
    num_c_seats = int(input('Enter the number of Class C seats to purchase: '))
    total_cost = (num_a_seats * CLASS_A_SEAT) + (num_b_seats *
                                                 CLASS_B_SEAT) + (num_c_seats * CLASS_C_SEAT)

    print('The total cost of the seats will be ${}'.format(total_cost))


main()
