number_of_allowed_bad_grades = int(input())

average_score = 0
number_of_problems = 0
bad_grades = 0
last_problem = ""

while True:
    name_of_exercise = input()

    if name_of_exercise == "Enough":
        print(f"Average score: {(average_score / number_of_problems):.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_problem}")
        break
    else:
        grade_for_the_exercise = int(input())
        last_problem = name_of_exercise
        if grade_for_the_exercise <= 4:
            bad_grades += 1
            if bad_grades >= number_of_allowed_bad_grades:
                print(f"You need a break, {bad_grades} poor grades.")
                break

    number_of_problems += 1
    average_score += grade_for_the_exercise

