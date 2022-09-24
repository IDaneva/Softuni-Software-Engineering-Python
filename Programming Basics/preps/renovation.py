import math

height_of_wall = int(input())
width_of_wall = int(input())
percent_that_wont_be_painted = int(input()) / 100

area_of_room = height_of_wall * width_of_wall * 4

area_that_will_be_painted_actually = math.ceil(area_of_room - (area_of_room * percent_that_wont_be_painted))


painted_area = 0

while True:
    litres_of_paint = input()

    if litres_of_paint == "Tired!":
        print(f"{abs(area_that_will_be_painted_actually - painted_area)} quadratic m left.")
        break

    else:
        painted_area += int(litres_of_paint)

        if painted_area > area_that_will_be_painted_actually:
            print(f"All walls are painted and you have {abs(area_that_will_be_painted_actually - painted_area)} l paint left!")
            break
        elif painted_area == area_that_will_be_painted_actually:
            print("All walls are painted! Great job, Pesho!")
            break
