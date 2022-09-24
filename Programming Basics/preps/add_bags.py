price_for_over_20_kg = float(input())
luggage_weight = float(input())
days_till_trip = int(input())
luggage_ammount = int(input())

costs = 0
if luggage_weight < 10:
    costs = 0.2 * price_for_over_20_kg
elif 10 <= luggage_weight <= 20:
    costs = price_for_over_20_kg * 0.5
elif luggage_weight > 20:
    costs = price_for_over_20_kg

if days_till_trip > 30:
    costs += 0.1 * costs
elif 7 <= days_till_trip <= 30:
    costs += 0.15 * costs
elif days_till_trip < 7:
    costs += 0.4 * costs

total = costs * luggage_ammount
print(f"The total price of bags is: {total:.2f} lv.")
