from collections import deque
duration_of_green_light = int(input())
duration_of_free_window = int(input())

cars = deque()
passed_cars = 0

crash = False

new_green_duration = duration_of_green_light
new_free_window_duration = duration_of_free_window

while True:
    command = input()
    if command == "END":
        break

    if command == "green":
        while True:
            if not cars or new_green_duration == 0:
                new_green_duration = duration_of_green_light
                new_free_window_duration = duration_of_free_window
                break
            first_car = cars.popleft()
            if len(first_car) <= new_green_duration:
                passed_cars += 1
                new_green_duration -= len(first_car)
                continue

            else:
                stopped = False
                for ch in first_car:
                    if new_green_duration > 0:
                        while new_green_duration > 0:
                            new_green_duration -= 1
                            break
                    elif new_free_window_duration > 0:
                        while new_free_window_duration > 0:
                            new_free_window_duration -= 1
                            break
                    else:
                        if new_free_window_duration == 0:
                            crash = True
                            print(f"A crash happened!")
                            print(f"{first_car} was hit at {ch}.")
                            break
                if not crash:
                    passed_cars += 1
                else:
                    break
    else:
        cars.append(command)

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")