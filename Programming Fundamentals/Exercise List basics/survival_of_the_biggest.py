list_of_string = input().split()
numbers_to_remove = int(input())

list_of_integer = [int(i) for i in list_of_string]

for _ in range(numbers_to_remove):
    min_number = min(list_of_integer)
    list_of_integer.remove(min_number)

print(", ".join(map(str, list_of_integer)))
