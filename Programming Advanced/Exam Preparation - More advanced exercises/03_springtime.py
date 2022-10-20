def start_spring(**kwargs):
    spring_dict = {}
    for value, key in kwargs.items():
        if key not in spring_dict:
            spring_dict[key] = []
        spring_dict[key].append(value)
    result_dict = dict(sorted(spring_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ""
    for k, v in result_dict.items():
        result += f"{k}:\n"
        for f in sorted(v):
            result += f"-{f}\n"
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
