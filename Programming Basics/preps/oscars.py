name_of_actor = input()
points_from_academy = float(input())
number_of_evaluators = int(input())
total = 0 + points_from_academy

condition = False

for _ in range(number_of_evaluators):
    name_of_evaluator = input()
    points_from_evaluator = float(input())

    total += ((len(name_of_evaluator)) * points_from_evaluator) / 2

    if total > 1250.5:
        condition = True
        break

if condition:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total:.1f}!")
else:
    diff = abs(1250.5 - total)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")