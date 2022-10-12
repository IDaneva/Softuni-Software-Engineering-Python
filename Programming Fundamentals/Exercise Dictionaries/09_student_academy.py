def find_average_grade(list_of_grades):
    average = sum(list_of_grades) / len(list_of_grades)
    return average


number_of_students = int(input())

grade_dict = {}

for _ in range(number_of_students):
    student_name = input()
    student_grade = float(input())

    if student_name not in grade_dict:
        grade_dict[student_name] = []
    grade_dict[student_name].append(student_grade)

for curent_student, grades in grade_dict.items():
    if find_average_grade(grades) >= 4.5:
        print(f"{curent_student} -> {(find_average_grade(grades)):.2f}")

