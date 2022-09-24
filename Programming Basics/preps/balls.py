import math

number = int(input())

points = 0
other_balls = 0
divides = 0
red = 0
orange = 0
yellow = 0
white = 0

for ball in range(number):
    colors = input()
    if colors == "red":
        points += 5
        red += 1
    elif colors == "orange":
        points += 10
        orange += 1
    elif colors == "yellow":
        points += 15
        yellow += 1
    elif colors == "white":
        points += 20
        white += 1
    elif colors == "black":
        points = math.floor(points/2)
        divides += 1
    else:
        other_balls += 1

print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {divides}")

