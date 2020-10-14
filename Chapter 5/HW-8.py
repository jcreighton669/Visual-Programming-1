import math

""" A painting company has determined that for every 112 square frrt of
wall space, one gallon of paint and eight hours of labor will be
required. The company charges $35.00 per hour for labor. Write a program
that asks the user to enter the square feet of wall space to be painted
and the price of the paint per gallon. The program should display the
following data: - The number of gallons of paint required - The hours of
labor required - The cost of the paint - The labor charges - The total
cost of the paint job """
# Constants
STANDARD_WALL_SPACE = 112
COST_PER_HOUR = 35.00
LABOR_PER_GALLON = 8


def main():
    # Input for the calculations
    wall_space_to_paint = int(
        input('Enter the square footage of the area to be painted: '))
    price_of_paint = int(input('Enter the cost of a gallon of paint: '))

    # Calculate the required paint
    gallons_required = wall_space_to_paint / STANDARD_WALL_SPACE
    gallons_required = math.ceil(gallons_required)
    print('Gallons of paint required: ', gallons_required)

    # Calculate the hours of labor required
    labor_required = gallons_required * LABOR_PER_GALLON
    print('Hours of labor required: ', labor_required)

    # Calculate cost of paint
    cost_of_paint = gallons_required * price_of_paint
    cost_of_paint = float(format(cost_of_paint, '.2f'))
    print("Cost of paint: $", cost_of_paint)

    # Calculate the cost of labor
    labor_cost = labor_required * COST_PER_HOUR
    labor_cost = float(format(labor_cost, '.2f'))
    print('Cost of labor: $', labor_cost)

    # Calculate the total cost of the job
    total_cost = cost_of_paint + labor_cost
    total_cost = float(format(total_cost, '.2f'))
    print('Total cost: $', total_cost)


main()
