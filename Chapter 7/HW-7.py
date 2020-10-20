"""
The local driver's license office has asked you to create an application that
grades the written portion of the driver's license exam. The exam has 20
mulitple-choice questions. Here are the correct answers:

ANSWERS = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C',
    'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

Your program should store these correct answers in a list. The program should
read the students answers for each of the 20 questions from a text file and
store the answers in another list. (Create your own text file to test the
application.) After the student's answers have been read from the file, the
program  should display a message indicating whether the student passed or
failed the exam. (A student must correctly answer 15 of the 20 questions to
pass the exam.) It should then display the total number of correctly answered
questions, the total number of incorrectly answered questions, and a list
showing the question numbers of the incorrectly answered questions.
"""

# Initialize the correct answers in a list
ANSWERS = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C',
           'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']


# Read in the file and add the student's answers to a list
def read_file(filename):
    student_answers = []
    fn = open(filename, 'r')
    line = fn.readline()
    while line != '':
        # Make sure that the student answer is capitalized and a single character
        student_answers.append(str(line[0]).upper())
        line = fn.readline()

    # Close the file after getting the information
    fn.close()
    print(student_answers)
    return student_answers


# Compare the student answers with the correct answers
def compare_answers(student_arr):
    correct_answers = ANSWERS
    correct_count = 0
    for i in range(20):
        if correct_answers[i] == student_arr[i]:
            correct_count += 1

    # Return the number of correct answers
    return correct_count


# Get the users information and run the functions
def main():
    student_file = input("Enter the filename path of the student answers: ")

    student_array = read_file(student_file)
    correct_ans = compare_answers(student_array)
    incorrect_answers = 20 - correct_ans
    final_score = 5 * correct_ans

    print("The total correct answers: \t\t", correct_ans)
    print("The total incorrect answers: \t\t", incorrect_answers)
    print("The final grade: \t\t", final_score)
    if correct_ans >= 15:
        print("The student has PASSED!")
    else:
        print("The student has failed.")


# Call the main function
main()
