number_of_evaluators = int(input())
total_grades = 0
students_counter = 0

current_presentation = ""
current_total = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break
    else:
        current_total = 0
        for _ in range(number_of_evaluators):
            grade_for_current_presentation = float(input())
            current_total += grade_for_current_presentation
            current_presentation = presentation_name
            students_counter += 1
            total_grades += grade_for_current_presentation
        print(f"{current_presentation} - {(current_total / number_of_evaluators):.2f}.")

average_of_total = total_grades / students_counter

print(f"Student's final assessment is {average_of_total:.2f}.")