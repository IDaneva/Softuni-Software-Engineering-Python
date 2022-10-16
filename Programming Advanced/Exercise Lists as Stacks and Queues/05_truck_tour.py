from collections import deque

number_of_stations = int(input())

stops = deque()

for current_station in range(number_of_stations):
    pump_info = [int(x) for x in input().split()]
    stops.append(pump_info)

for attempt in range(number_of_stations):
    tank = 0
    failed = False
    for gas, km in stops:
        tank += gas
        if tank < km:
            failed = True
            break
        else:
            tank -= km
    if failed:
        stops.append(stops.popleft())
    else:
        print(attempt)
        break





