def pw_data_base_generator(password_info):
    while True:
        command = input()
        if command == "end of contests":
            break
        command = command.split(":")
        contest_name = command[0]
        pw_for_contest = command[1]
        if contest_name not in password_info:
            password_info[contest_name] = pw_for_contest

    return password_info


def student_info_compiler(student_data_base, password_info):
    while True:
        command = input()
        if command == "end of submissions":
            break
        command = command.split("=>")
        contest = command[0]
        password = command[1]
        username = command[2]
        points = int(command[3])

        if contest in password_info and password == password_info[contest]:
            if username not in student_data_base:
                student_data_base[username] = {contest: points}
            elif contest not in student_data_base[username]:
                student_data_base[username][contest] = points
            else:
                if points > student_data_base[username][contest]:
                    student_data_base[username][contest] = points
        else:
            continue
    return student_data_base


password_info = {}
pw_data_base_generator(password_info)
student_data_base = {}
student_info_compiler(student_data_base, password_info)

best_candidate = ""
max_points = 0

for current_student, exam_info in student_data_base.items():
    total_points = 0
    for current_exam, received_points in exam_info.items():
        total_points += received_points
    if total_points >= max_points:
        max_points = total_points
        best_candidate = current_student

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print(f"Ranking:")

# sorted_names = sorted(student_data_base.keys())
# sorted_points = ""
# for student_name, his_info in student_data_base.items():
#     for exam_name, points in his_info.items():
#         sorted_points = sorted(his_info.values())
#     print(f"")

# student_data_base = sorted(student_data_base.values())
print(student_data_base)