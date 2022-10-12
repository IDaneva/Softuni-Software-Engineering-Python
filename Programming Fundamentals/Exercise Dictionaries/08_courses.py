course_information = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name not in course_information:
        course_information[course_name] = []
    course_information[course_name].append(student_name)

print(course_information)

for current_course, registered_students in course_information.items():
    print(f"{current_course}: {len(registered_students)}")
    for students in registered_students:
        print(f"-- {students}")
