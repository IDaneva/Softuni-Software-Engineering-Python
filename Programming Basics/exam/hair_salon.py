target_for_the_day = int(input())

money_earned = 0

condition = False
type = ""

while True:
    command = input()

    if command == "closed":
        break

    if command == "haircut":
        type = input()
        if type == "mens":
            money_earned += 15
        elif type == "ladies":
            money_earned += 20
        elif type == "kids":
            money_earned += 10
    elif command == "color":
        type = input()
        if type == "touch up":
            money_earned += 20
        elif type == "full color":
            money_earned += 30

    if money_earned >= target_for_the_day:
        condition = True
        break

diff = abs(target_for_the_day - money_earned)

if condition:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {int(diff)}lv. more.")

print(f"Earned money: {int(money_earned)}lv.")