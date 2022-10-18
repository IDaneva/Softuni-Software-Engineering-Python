def numbers_searching(*nums):
    no_duplicates = []
    duplicates = []
    for n in nums:
        if n not in no_duplicates:
            no_duplicates.append(n)
        else:
            if n in duplicates:
                continue
            duplicates.append(n)

    max_num = max(no_duplicates)
    min_num = min(no_duplicates)
    missing = ''
    for current in range(min_num, max_num):
        if current not in no_duplicates:
            missing = current
    return [missing, sorted(duplicates)]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(1, 2, 4, 2, 5, 4))
