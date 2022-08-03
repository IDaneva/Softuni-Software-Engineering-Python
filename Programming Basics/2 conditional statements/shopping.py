budget = float(input())
videocards_amount = int(input())
processors_amount = int(input())
ram_amount = int(input())

videocards_price = 250
bought_video_cards = videocards_price * videocards_amount

processors_price = bought_video_cards * 0.35
ram_price = bought_video_cards * 0.1

total = videocards_price * videocards_amount + processors_price * processors_amount + ram_price * ram_amount

if videocards_amount > processors_amount:
    total -= 0.15 * total

diff = abs(budget - total)

if budget >= total:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
