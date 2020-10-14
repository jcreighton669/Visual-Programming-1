"""
A nutritionist who works for a fitness club helps members by evaluating their 
diets. As part of her evaluation, she asks members for the number of fat grams 
and carbohydrate grams that they consumed in a day. Then, she calculates the 
number of calories that result from the fat, using the following formula:

calories from fat = fat grams * 9

Next, she calculates the number of calories that result from the carbohydrates, 
using the following formula:

calories from carbs = carb grams * 4

The nutritionist asks you to write a program that will make these calculations.
"""


def main():
    fat_grams = int(input('Enter the number of grams of fat consumed: '))
    carb_grams = int(input('Enter the number of grams of carb consumed: '))

    fat_calories = fat_grams * 9
    carb_calories = carb_grams * 4

    print('The member consumed {} calories of fat and {} calories of carbs'.format(
        fat_calories, carb_calories))


main()
