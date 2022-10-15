def find_name(letter, *args):
    for name in args:
        if name.startswith(letter):
            return name


def age_assignment(*args, **kwargs):
    person_info = {}
    result = ""

    for letter, age in kwargs.items():
        name = find_name(letter, *args)
        person_info[name] = age

    sorted_info = dict(sorted(person_info.items()))
    for k, v in sorted_info.items():
        result += f"{k} is {v} years old." + "\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))
