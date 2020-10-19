"""
Write a program that reads the file's contents into a list. The program should
display the following data:
	* The average annual change in population during the time period
	* The year with the greatest increase in population during the time period
	* The year with the smallest increase in population during the time period
"""


def read_file(filename):
    annual_population = []
    fn = open(filename, 'r')
    for line in fn:
        annual_population.append(int(line))

    fn.close()

    return annual_population


def calc_difference(num1, num2):
    return num2 - num1


def increase_array(arr):

    pop_change = []
    for i in range(len(arr) - 1):
        pop_change.append(calc_difference(arr[i], arr[i+1]))

    return pop_change


def calc_average(arr):
    population_flux = 0
    sum = 0
    count = 0
    for num in arr:
        sum += int(num)
        count += 1

    population_flux = sum / count
    return population_flux


def main():
    filename = input("Enter the population file address: ")
    pop_arr = read_file(filename)
    population_increase = increase_array(pop_arr)
    max_increase = population_increase.index(max(population_increase)) + 1951
    min_increase = population_increase.index(min(population_increase)) + 1951
    avg_increase = int(calc_average(population_increase))
    print("The average annual change in population during the time period is",
          avg_increase, "thousand")
    print("The year with the greatest increase in population during the time period was",
          max_increase)
    print("The year with the smallest increase in population during the time period was",
          min_increase)


main()
