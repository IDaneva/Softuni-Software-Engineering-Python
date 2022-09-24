price_for_tshirt = float(input())
sum_he_has_to_achieve_for_ball = float(input())

shorts_price = price_for_tshirt * 0.75
socks_price = shorts_price * 0.2
shoes = (price_for_tshirt + shorts_price) * 2

# print(shorts_price)
# print(socks_price)
# print(shoes)

total = price_for_tshirt + shorts_price + socks_price + shoes

total_with_discount = total - (total * 0.15)

diff = abs(sum_he_has_to_achieve_for_ball - total_with_discount)

if total_with_discount >= sum_he_has_to_achieve_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_with_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")