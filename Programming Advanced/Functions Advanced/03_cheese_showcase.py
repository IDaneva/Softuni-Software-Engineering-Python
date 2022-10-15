def sorting_cheeses(**kwargs):
    str_to_print = ""
    result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in result:
        descending_list = sorted([int(x) for x in value], reverse=True)
        str_to_print += key + "\n" + "\n".join(map(str, descending_list)) + "\n"
    return str_to_print


print(sorting_cheeses(
Parmesan=[102, 120, 135],
Camembert=[100, 100, 105, 500, 430],
Mozzarella=[50, 125],))

