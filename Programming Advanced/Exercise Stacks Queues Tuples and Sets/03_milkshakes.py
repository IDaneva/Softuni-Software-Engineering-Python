from collections import deque

choco = list(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))
made_milkshakes = 0

while choco and milk_cups:
    last_choco = choco[-1]
    first_cup = milk_cups[0]
    flag = True

    if made_milkshakes == 5:
        break

    if last_choco <= 0:
        choco.pop()
        flag = False

    if first_cup <= 0:
        milk_cups.popleft()
        flag = False

    if not flag:
        continue

    elif last_choco == first_cup:
        made_milkshakes += 1
        choco.pop()
        milk_cups.popleft()

    else:
        milk_cups.append(milk_cups.popleft())
        choco[-1] -= 5


if made_milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if choco:
    print(f"Chocolate: {', '.join(list(map(str, choco)))}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(list(map(str, milk_cups)))}")
else:
    print("Milk: empty")
