def problem_fixed_question():

    answer = input("\nDid that fix the problem: ")
    return answer


def main():
    print("Reboot the computer and try to connect. ")
    answer = problem_fixed_question()
    if answer.lower().startswith('n'):
        print("Reboot the router and try to connect. ")
        answer = problem_fixed_question()
        if answer.lower().startswith('n'):
            print(
                "Make sure the cables between the router & modem are plugged in firmly. ")
            answer = problem_fixed_question()
            if answer.lower().startswith('n'):
                print("Move the router to a new location and try to connect.")
                answer = problem_fixed_question()
                if answer.lower().startswith('n'):
                    print("Get a new router.")


main()
