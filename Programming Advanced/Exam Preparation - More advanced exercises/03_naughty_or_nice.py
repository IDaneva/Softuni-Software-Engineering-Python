def naughty_or_nice_list(list_of_names, *args, **kwargs):
    dict_info = {}

    for kid in list_of_names:
        id, name = kid
        if id not in dict_info:
            dict_info[id] = []
        dict_info[id].append(name)

    result = {"Nice": [], "Naughty": [], "Not found": []}

    for command in args:
        num, instructions = command.split("-")
        if instructions == "Nice" and int(num) in dict_info:
            if len(dict_info[int(num)]) == 1:
                result["Nice"].extend(dict_info[int(num)])
                del dict_info[int(num)]
            else:
                continue
        elif instructions == "Naughty" and int(num) in dict_info:
            if len(dict_info[int(num)]) == 1:
                result["Naughty"].extend(dict_info[int(num)])
                del dict_info[int(num)]
            else:
                continue
    if kwargs:
        for value, key in kwargs.items():
            found_times = 0
            for num, names in dict_info.items():
                found_times += names.count(value)

            if found_times == 1:
                result[key].append(value)
                for k, v in dict_info.items():
                    if value in v:
                        dict_info[k].remove(value)
                        break
            else:
                continue

    for last_nums, last_names in dict_info.items():
        result["Not found"].extend(dict_info[last_nums])

    result_to_print = ""

    for category in result:
        if result[category]:
            result_to_print += f"{category}: {', '.join(result[category])}\n"

    return result_to_print


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
#
#
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
