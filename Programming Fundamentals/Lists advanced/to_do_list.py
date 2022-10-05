to_dos = []

while True:
    events = input()
    if events == "End":
        break
    else:
        data = events.split("-")
        priority = int(data[0])
        note = data[1]
        to_dos.append((priority, note))

sorted_tasks = [task_data[1] for task_data in sorted(to_dos)]
print(sorted_tasks)