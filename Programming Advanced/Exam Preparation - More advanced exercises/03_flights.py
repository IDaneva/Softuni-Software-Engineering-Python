from collections import deque


def flights(*flight_info):
    info_dict = {}
    flight_info = deque(flight_info)
    while flight_info:
        current_flight = flight_info.popleft()
        if current_flight == "Finish":
            break
        current_passenger_count = flight_info.popleft()
        if current_flight not in info_dict:
            info_dict[current_flight] = 0
        info_dict[current_flight] += int(current_passenger_count)

    return info_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
