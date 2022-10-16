from collections import deque

quantity_of_food_for_day = int(input())
quantity_in_each_order = deque([int(s) for s in input().split()])

biggest_order = max(quantity_in_each_order)
print(biggest_order)

success = True

while len(quantity_in_each_order) > 0:
    first_in_queue = quantity_in_each_order[0]
    if first_in_queue <= quantity_of_food_for_day:
        quantity_of_food_for_day -= first_in_queue
        quantity_in_each_order.popleft()
    else:
        success = False
        break

if not success:
    print(f"Orders left: {' '.join([str(i) for i in quantity_in_each_order])}")
else:
    print("Orders complete")
