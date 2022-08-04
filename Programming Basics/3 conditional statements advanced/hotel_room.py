month = input()
nights_per_stay = int(input())

if month == "May" or month == "October":
    studio_cost = 50
    apartment_cost = 65
    if nights_per_stay > 7 and nights_per_stay <= 14:
        studio_cost -= studio_cost * 0.05
    elif nights_per_stay > 14:
        studio_cost -= studio_cost * 0.30
        apartment_cost -= apartment_cost * 0.10
elif month == "June" or month == "September":
    studio_cost = 75.20
    apartment_cost = 68.70
    if nights_per_stay > 14:
        studio_cost -= studio_cost * 0.20
        apartment_cost -= apartment_cost * 0.10
elif month == "July" or month == "August":
    studio_cost = 76
    apartment_cost = 77
    if nights_per_stay > 14:
        apartment_cost -= apartment_cost * 0.10

total_apartment_cost = apartment_cost * nights_per_stay
total_studio_cost = studio_cost * nights_per_stay

print(f"Apartment: {total_apartment_cost:.2f} lv.")
print(f"Studio: {total_studio_cost:.2f} lv.")
