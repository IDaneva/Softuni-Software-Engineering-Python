from collections import deque


def bomb_creator(n):
    for bomb in bomb_types:
        if bomb_types[bomb][0] == n:
            bomb_types[bomb][1] += 1
            return True
    return False


def bomb_checker():
    if bomb_types["Datura Bombs"][1] >= 3 \
            and bomb_types["Cherry Bombs"][1] >= 3 \
            and bomb_types["Smoke Decoy Bombs"][1] >= 3:
        return True


bomb_types = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Decoy Bombs": [120, 0]
}

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = deque([int(x) for x in input().split(", ")])

while True:
    if not bomb_effects or not bomb_casings:
        break

    first_bomb_effect = bomb_effects.popleft()
    last_bomb_casing = bomb_casings.pop()

    number_to_check = first_bomb_effect + last_bomb_casing
    if bomb_creator(number_to_check):
        if bomb_checker():
            break
        else:
            continue
    else:
        last_bomb_casing -= 5
        bomb_casings.append(last_bomb_casing)
        bomb_effects.appendleft(first_bomb_effect)
        continue

if bomb_checker():
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(list(map(str, bomb_effects)))}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(list(map(str, bomb_casings)))}")
else:
    print("Bomb Casings: empty")

sorted_dict = dict(sorted(bomb_types.items(), key= lambda x: x[0]))

for k, v in sorted_dict.items():
    print(f"{k}: {v[1]}")
