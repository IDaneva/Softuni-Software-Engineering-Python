budget = float(input())
statisti= int(input())
price_for_clothes_per_statist = float(input())

decor = budget * 0.1

total_for_clothes = statisti * price_for_clothes_per_statist

if statisti > 150:
    total_for_clothes -= 0.1 * total_for_clothes

expenses = decor + total_for_clothes
diff = abs(budget - expenses)

if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
