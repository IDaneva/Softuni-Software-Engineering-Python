number_of_dancers = int(input())
points = float(input())

season = input()
place = input()

costs = 0
if place == "Bulgaria":
    earned_money = number_of_dancers * points
    if season == "summer":
        earned_money -= earned_money * 0.05
    elif season == "winter":
        earned_money -= earned_money * 0.08
elif place == "Abroad":
    earned_money = number_of_dancers * points
    earned_money += 0.5 * earned_money
    if season == "summer":
        earned_money -= earned_money * 0.1
    elif season == "winter":
        earned_money -= earned_money * 0.15

charity = 0.75 * earned_money
earned_money -= charity

per_dancer = earned_money / number_of_dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {per_dancer:.2f}")
