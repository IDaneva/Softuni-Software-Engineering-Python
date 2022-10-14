from collections import deque

working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
made_honey = 0

while working_bees and nectar:
    first_bee = working_bees[0]
    last_nectar = nectar[-1]
    if last_nectar >= first_bee:
        current_operation = symbols[0]
        if current_operation == "+":
            made_honey += abs(first_bee + last_nectar)
        elif current_operation == "-":
            made_honey += abs(first_bee - last_nectar)
        elif current_operation == "*":
            made_honey += abs(first_bee * last_nectar)
        elif current_operation == "/":
            if last_nectar != 0:
                made_honey += abs(first_bee / last_nectar)
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()
        continue

print(f"Total honey made: {made_honey}")
if working_bees:
    print(f"Bees left: {', '.join(list(map(str, working_bees)))}")
if nectar:
    print(f"Nectar left: {', '.join(list(map(str, nectar)))}")
