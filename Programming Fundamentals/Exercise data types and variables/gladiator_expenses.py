number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
broken_shields = 0

for games in range(1, number_of_lost_fights + 1):
    if games % 2 == 0:
        total_expenses += helmet_price
    if games % 3 == 0:
        total_expenses += sword_price
    if games % 6 == 0:
        total_expenses += shield_price
        broken_shields += 1
    if broken_shields > 0 and broken_shields % 2 == 0:
        total_expenses += armor_price
        broken_shields = 0

print(f"Gladiator expenses: {total_expenses:.2f} aureus")