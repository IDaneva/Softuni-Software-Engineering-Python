from collections import deque


def firework_collector():
    if made_fireworks["Palm Fireworks"] >= 3 \
            and made_fireworks["Willow Fireworks"] >= 3\
            and made_fireworks["Crossette Fireworks"] >= 3:
        return True
    else:
        return False


made_fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

success = False

while True:

    if not effects or not explosive_power:
        if firework_collector():
            success = True
        break
    if firework_collector():
        success = True
        break

    first_firework_effect = effects.popleft()
    if first_firework_effect <= 0:
        continue
    last_explosive_power = explosive_power.pop()
    if last_explosive_power <= 0:
        effects.appendleft(first_firework_effect)
        continue

    mix = first_firework_effect + last_explosive_power

    if mix % 3 == 0 and mix % 5 != 0:
        made_fireworks["Palm Fireworks"] += 1
        continue

    elif mix % 5 == 0 and mix % 3 != 0:
        made_fireworks["Willow Fireworks"] += 1
        continue

    elif mix % 3 == 0 and mix % 5 == 0:
        made_fireworks["Crossette Fireworks"] += 1
        continue

    else:
        first_firework_effect -= 1
        effects.append(first_firework_effect)
        explosive_power.append(last_explosive_power)

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(list(map(str, effects)))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(list(map(str, explosive_power)))}")

for k, v in made_fireworks.items():
    print(f"{k}: {v}")
