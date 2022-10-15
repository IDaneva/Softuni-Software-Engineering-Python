def even_odd_filter(**kwargs):
    dict_info = {}

    def even(nums):
        return [i for i in nums if i % 2 == 0]

    def odd(nums):
        return [i for i in nums if i % 2 != 0]

    for key, value in kwargs.items():
        if key == "even":
            dict_info[key] = even(value)
        else:
            dict_info[key] = odd(value)

    return dict(sorted(dict_info.items(), key= lambda x: -len(x[1])))


print(even_odd_filter(

odd=[1, 2, 3, 4, 10, 5],

even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))