number_of_names = int(input())

student_info = {}

for _ in range(number_of_names):
    students = input().split()
    name = students[0]
    grade = float(students[1])
    if name not in student_info:
        student_info[name] = ([], [])
    student_info[name][0].append(f"{grade:.2f}")
    student_info[name][1].append(grade)


for key, value in student_info.items():
    print(f"{key} -> {' '.join(value[0])} (avg: {(sum(value[1])/len(value[1])):.2f})")
