amount_to_transport = int(input())

micro_bus = 0
bus = 0
train = 0

for _ in range(amount_to_transport):
    weight = int(input())
    if weight <= 3:
        price_for_tone_microbus = 200
        micro_bus += weight

    elif 4 <= weight <= 11:
        price_for_tone_bus = 175
        bus += weight

    elif weight >= 12:
        price_for_tone_train = 120
        train += weight

total_weight = micro_bus + bus + train

average_pro_tone = (micro_bus * 200 + bus * 175 + train * 120) / total_weight

print(f"{average_pro_tone:.2f}")
print(f"{(micro_bus/total_weight * 100):.2f}%")
print(f"{(bus/total_weight * 100):.2f}%")
print(f"{(train/total_weight * 100):.2f}%")

