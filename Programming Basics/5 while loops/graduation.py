total = 0

class_counter = 0

name = input()
bad_grades = 0

condition = False

while class_counter < 12:
    grade = float(input())

    if grade < 4:
        bad_grades += 1
        if bad_grades > 1:
            condition = True
            class_counter += 1
            print(f"{name} has been excluded at {class_counter} grade")
            break
    else:
        total += grade
        class_counter += 1

average = total/12
if not condition:
    print(f"{name} graduated. Average grade: {average:.2f}")


