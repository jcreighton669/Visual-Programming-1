"""
Write a program that gives simple math quizzes. The program should display two
random numbers that are to be added, such as:
	247
+	129
The program should allow the student to enter the answer. If the answer is
correct, a message of congratulations should be displayed. If the answer is
incorrect, a message showing the correct answer should be displayed.
"""

import random


def generate_question():
    # Generate 2 random integers between 1 and 1000
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)

    # Print the math problem
    print('\t', num1)
    print('+\t', num2)
    sum = num1 + num2

    # Return the correct answer
    return sum


def main():
    correct_answer = generate_question()
    guessed_answer = int(input('Guess the correct answer: '))

    # Compare the user input with the correct answer
    if correct_answer == guessed_answer:
        print('Congratulations! That is correct.')
    else:
        print("Sorry that is incorrect, the correct answer is", correct_answer)


main()
