numbers = list(map(int, input().split(", ")))
# even_numbers = [numbers.index(current_number) for current_number in numbers if current_number % 2 == 0]
even_numbers = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(even_numbers)
