def positive_function(nums):
    return [number for number in nums if int(number) >= 0]


def negative_function(nums):
    return [number for number in nums if int(number) < 0]


def even_function(nums):
    return [number for number in nums if int(number) % 2 == 0]


def odd_function(nums):
    return [number for number in nums if int(number) % 2 != 0]


numbers = input().split(", ")

print(f"Positive: {', '.join(positive_function(numbers))}")
print(f"Negative: {', '.join(negative_function(numbers))}")
print(f"Even: {', '.join(even_function(numbers))}")
print(f"Odd: {', '.join(odd_function(numbers))}")
