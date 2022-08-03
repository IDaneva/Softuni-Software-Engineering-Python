length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())

capacity_tank = length_in_cm * width_in_cm * height_in_cm
capacity_litres = capacity_tank / 1000

needed_litres = capacity_litres * (1 - (percentage / 100))

print(needed_litres)
