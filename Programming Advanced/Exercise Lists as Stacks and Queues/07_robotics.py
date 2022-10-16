from collections import deque

robots_info = input().split(";")
start_time = [int(x) for x in input().split(":")]

name_and_process_time = {}
machine_deque = deque()

for current in robots_info:
    name, time = current.split("-")
    name_and_process_time[name] = {"needed_time": int(time), "start_time": [], "free_at": [], "free": True}
    machine_deque.append(name)

products_deque = deque()

while True:
    command = input()
    start_time[2] += 1

    if start_time[2] == 60:
        start_time[2] = 0
        start_time[1] += 1
    if start_time[1] == 60:
        start_time[1] = 0
        start_time[0] += 1
        if start_time[0] == 24:
            start_time[0] = 0
            start_time[1] = 0
            start_time[2] = 0

    if command == "End":
        break
    product = command
    while True:
        robot = machine_deque[0]
        if name_and_process_time[robot]["free_at"] == start_time:
            name_and_process_time[robot]["free"] = True

        if name_and_process_time[robot]["free"]:
            name_and_process_time[robot]["start_time"] = start_time
            result = []
            for i in name_and_process_time[robot]["start_time"]:
                result.append(str(f"{i:02d}"))

            name_and_process_time[robot]["free_at"] = [start_time[0], start_time[1], start_time[2] + name_and_process_time[robot]["needed_time"]]
            name_and_process_time[robot]["free"] = False
            print(f"{robot} - {product} [{':'.join(result)}]")
            machine_deque.append(machine_deque.popleft())
            break

        machine_deque.append(machine_deque.popleft())
        products_deque.append(product)
        start_time[2] += 1

