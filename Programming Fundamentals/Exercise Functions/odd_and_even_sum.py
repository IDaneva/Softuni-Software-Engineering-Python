def even_sum(number):
    evens = 0
    for x in number:
        if int(x) % 2 == 0:
            evens += int(x)
    return evens


def odd_sum(number):
    odds = 0
    for x in number:
        if int(x) % 2 != 0:
            odds += int(x)
    return odds


input_number = input()
print(f"Odd sum = {odd_sum(input_number)}, Even sum = {even_sum(input_number)}")
