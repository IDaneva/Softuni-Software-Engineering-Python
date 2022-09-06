goal = 10000
total_steps = 0

while total_steps < goal:
    steps_made = input()

    if steps_made == "Going home":
        more_steps = int(input())
        total_steps += more_steps
        break

    total_steps += int(steps_made)

diff = int(abs(goal - total_steps))

if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")