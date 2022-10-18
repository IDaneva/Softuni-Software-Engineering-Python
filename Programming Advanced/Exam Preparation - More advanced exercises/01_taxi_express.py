from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while True:
    if not customers or not taxis:
        break
    first_customer = customers.popleft()
    last_taxi = taxis.pop()
    if first_customer <= last_taxi:
        total_time += first_customer
        continue
    else:
        customers.appendleft(first_customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(list(map(str, customers)))}")
