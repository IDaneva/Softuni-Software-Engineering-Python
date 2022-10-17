from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while True:
    if not bowls_of_ramen or not customers:
        break
    last_bowl = bowls_of_ramen.pop()
    first_customer = customers.popleft()

    if last_bowl == first_customer:
        continue
    elif last_bowl > first_customer:
        last_bowl -= first_customer
        bowls_of_ramen.append(last_bowl)
    elif last_bowl < first_customer:
        first_customer -= last_bowl
        customers.appendleft(first_customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(list(map(str, bowls_of_ramen)))}")
elif not bowls_of_ramen:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(list(map(str, customers)))}")
