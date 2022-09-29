factor = int(input())
count = int(input())
list_of_multiplies = []
for number in range(1, count + 1):
    current_multiplication = number * factor
    list_of_multiplies.append(current_multiplication)
print(list_of_multiplies)