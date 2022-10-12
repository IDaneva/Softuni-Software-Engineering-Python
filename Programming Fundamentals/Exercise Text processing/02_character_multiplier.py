def smaller_length_finders(first_string, second_string):
    if len(first_string) > len(second_string):
        return second_string
    elif len(first_string) == len(second_string):
        return first_string
    else:
        return first_string


first_string, second_string = input().split(' ')

total_sum = 0

for index in range(0, len(smaller_length_finders(first_string, second_string))):
    total_sum += ord(first_string[index]) * ord(second_string[index])

if len(first_string) > len(second_string):
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
else:
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])

print(total_sum)