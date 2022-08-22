money = float(input())

year_till_he_has_to_live = int(input())

spends = 0
age = 18 - 1

for year in range(1800, year_till_he_has_to_live + 1):
    age += 1
    if year % 2 == 0:
        spends += 12000
    elif year % 2 != 0:
        spends += 12000 + (50 * age)


diff = abs(money - spends)

if money >= spends:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")