numbers = input().split()
reverse_nums = []
while len(numbers) > 0:
    last = numbers.pop()
    reverse_nums.append(last)
print(" ".join(reverse_nums))
