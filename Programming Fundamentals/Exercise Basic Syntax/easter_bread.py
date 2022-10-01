budget = float(input())
flour_price = float(input())
pack_of_eggs_price = flour_price * 0.75
litre_of_milk_price = (flour_price * 0.25) + flour_price
load_of_bread_price = litre_of_milk_price / 4
colored_eggs = 0

recipe_cost = pack_of_eggs_price + flour_price + load_of_bread_price

loaves = budget // recipe_cost
money_left = budget % recipe_cost

for made_loaves in range(1, int(loaves) + 1):
    colored_eggs += 3
    if made_loaves % 3 == 0:
        colored_eggs -= made_loaves - 2

print(f"You made {int(loaves)} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")