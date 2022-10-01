quantity_of_decorations = int(input())
days_till_christmas = int(input())

expenses = 0
christmas_spirit = 0

for days in range(1, days_till_christmas + 1):
    if days % 11 == 0:
        quantity_of_decorations += 2
    if days % 2 == 0:
        expenses += 2 * quantity_of_decorations
        christmas_spirit += 5
    if days % 3 == 0:
        expenses += 8 * quantity_of_decorations
        christmas_spirit += 13
    if days % 5 == 0:
        expenses += 15 * quantity_of_decorations
        christmas_spirit += 17
        if days % 3 == 0:
            christmas_spirit += 30
    if days % 10 == 0:
        christmas_spirit -= 20
        expenses += 23
if days_till_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {int(expenses)}")
print(f"Total spirit: {christmas_spirit}")