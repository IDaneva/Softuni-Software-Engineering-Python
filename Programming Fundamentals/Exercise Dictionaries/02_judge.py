def contest_day_information(judge_contest_info):
    while True:
        command = input()
        if command == "no more time":
            break
        command = command.split(" -> ")
        username = command[0]
        contest = command[1]
        points = int(command[2])
        if contest not in judge_contest_info:
            judge_contest_info[contest] = {username: points}
        else:
            if username not in judge_contest_info[contest]:
                judge_contest_info[contest][username] = points
            else:
                if points > judge_contest_info[contest][username]:
                    judge_contest_info[contest][username] = points

    return judge_contest_info


judge_contest_info = {}
contest_day_information(judge_contest_info)

for contest, student_info in judge_contest_info.items():
    print(f"{contest}: {len(student_info)} participants")
    for current_student, earned_points in student_info.items():
        print(f"{current_student} <::> {earned_points}")
