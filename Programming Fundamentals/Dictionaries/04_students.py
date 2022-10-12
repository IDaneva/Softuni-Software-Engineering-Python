dict_data = {}

while True:
    information = input()
    if ":" not in information:
        taken_module = information
        break
    name_ID_course = information.split(":")
    course = name_ID_course[2]
    student_info = f" {name_ID_course[0]} - {name_ID_course[1]} "

    if course not in dict_data:
        dict_data[course] = [student_info]
    else:
        dict_data[course].append(student_info)


for info in dict_data.get(taken_module.replace("_", " ")):
    print(info)

