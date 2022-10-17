def words_sorting(*args):
    word_dict = {}
    for word in args:
        word_dict[word] = sum([ord(x) for x in word])
    result = ""
    sum_of_all_values = sum(word_dict.values())
    if sum_of_all_values % 2 == 0:
        sorted_info = dict(sorted(word_dict.items(), key=lambda x: x[0]))
        for w, v in sorted_info.items():
            result += f"{w} - {v}\n"
    elif sum_of_all_values % 2 != 0:
        sorted_info = dict(sorted(word_dict.items(), key=lambda x: -x[1]))
        for w, v in sorted_info.items():
            result += f"{w} - {v}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'))
