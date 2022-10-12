exam_info = {}

while True:
    command = input()
    if command == "exam finished":
        break
    if "banned" in command:
        username, banned_event = command.split("-")
        for key, value in exam_info.items():
            for k, v in value.items():
                if username in k:
                    exam_info[key][k] = ["banned"]
    else:
        username, language, points = command.split("-")
        if language not in exam_info:
            exam_info[language] = {username: [int(points)]}
        else:
            if username not in exam_info[language]:
                exam_info[language][username] = [int(points)]
            else:
                exam_info[language][username].append(int(points))

# print(exam_info)
print("Results:")
for current_language, student_info in exam_info.items():
    for current_student, received_points in student_info.items():
        if "banned" not in exam_info[current_language][current_student]:
            print(f"{current_student} | {max(exam_info[current_language][current_student])}")

print("Submissions:")
for current_language, student_info in exam_info.items():
    submissions = 0
    for student_name, earned_points in student_info.items():
        submissions += len(earned_points)
    print(f"{current_language} - {submissions}")


