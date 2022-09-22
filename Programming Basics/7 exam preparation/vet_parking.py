number_of_days = int(input())

number_of_hours = int(input())

total = 0

for days in range(1, number_of_days + 1):
    price_per_day = 0

    for hours in range(1, number_of_hours + 1):
        if days % 2 == 0 and hours % 2 != 0:
            price_per_day += 2.5
            total += 2.5
        elif days % 2 != 0 and hours % 2 == 0:
            price_per_day += 1.25
            total += 1.25
        else:
            price_per_day += 1
            total += 1

    print(f"Day: {days} - {price_per_day:.2f} leva")

print(f"Total: {total:.2f} leva")
