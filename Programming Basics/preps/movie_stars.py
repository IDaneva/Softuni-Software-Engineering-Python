budget_for_actors = float(input())
condition = True

while True:
    name_of_actor = input()

    if name_of_actor == "ACTION":
        break

    if len(name_of_actor) > 15:
        salary = budget_for_actors * 0.2
    else:
        salary = float(input())

    budget_for_actors -= salary

    if budget_for_actors < 0:
        condition = False
        break

diff = abs(budget_for_actors)

if not condition:
    print(f"We need {diff:.2f} leva for our actors.")
else:
    print(f"We are left with {diff:.2f} leva.")



