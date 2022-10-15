def sort_nums(nums: list, command: str):
    if command == "positive":
        return sum([i for i in nums if i > 0])
    else:
        return sum([i for i in nums if i < 0])


numbers = [int(x) for x in input().split()]
negs = sort_nums(numbers, "negative")
pos = sort_nums(numbers, "positive")
print(negs)
print(pos)
if abs(negs) > pos:
    print("The negatives are stronger than the positives")
elif abs(negs) < pos:
    print("The positives are stronger than the negatives")
