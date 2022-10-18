from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employee_pizza_making_capacity = deque([int(x) for x in input().split(", ")])

completed_orders = 0

while True:

    if not pizza_orders or not employee_pizza_making_capacity:
        break

    first_order = pizza_orders.popleft()

    if first_order > 10 or first_order <= 0:
        continue

    last_employee_capacity = employee_pizza_making_capacity.pop()

    if first_order <= last_employee_capacity:
        completed_orders += first_order
    else:
        completed_orders += last_employee_capacity
        first_order -= last_employee_capacity
        pizza_orders.appendleft(first_order)

if not pizza_orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {completed_orders}")
    print(f"Employees: {', '.join(list(map(str, employee_pizza_making_capacity)))}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(list(map(str, pizza_orders)))}")





