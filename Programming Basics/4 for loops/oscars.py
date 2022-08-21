actor = input()
academy_points = float(input())
evaluators = int(input())

points_given = 0

for _ in range(evaluators):
    name_of_evaluator = input()
    points_from_evaluator = float(input())
    points_given += len(name_of_evaluator) * points_from_evaluator / 2
    total_points = academy_points + points_given

    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {(1250.5 - total_points):.1f} more!")
