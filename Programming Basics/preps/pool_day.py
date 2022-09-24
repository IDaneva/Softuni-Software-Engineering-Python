import math

ammount_of_people = int(input())
entering_price = float(input())
price_for_bed = float(input())
umbrella_price = float(input())

total_price_for_entering = ammount_of_people * entering_price
needed_beds = math.ceil(ammount_of_people * 0.75)
total_price_for_beds = needed_beds * price_for_bed
needed_umbrellas = math.ceil(ammount_of_people * 0.5)
total_price_for_umbrellas = needed_umbrellas * umbrella_price

total_price = total_price_for_beds + total_price_for_umbrellas + total_price_for_entering

print(f"{total_price:.2f} lv.")