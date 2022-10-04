import math


def find_coordinates(a, b):
    closest_coordinate = ""
    sum1 = 0
    sum2 = 0
    for current_coordinate1 in a:
        sum1 += abs(current_coordinate1)
    for current_coordinate2 in b:
        sum2 += abs(current_coordinate2)
    if sum1 > sum2:
        closest_coordinate = b
    elif sum1 == sum2:
        closest_coordinate = a
    else:
        closest_coordinate = a
    return closest_coordinate


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point_A = [x1, y1]
point_B = [x2, y2]


result = [math.floor(s) for s in find_coordinates(point_A, point_B)]
print(tuple(result))
