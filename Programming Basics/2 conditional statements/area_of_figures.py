import math

figure_type = input()

if figure_type == "square":
    square_side = float(input())
    area_square = square_side * square_side
    print("{0:.3f}".format(area_square))
if figure_type == "rectangle":
    rectangle_side1 = float(input())
    rectangle_side2 = float(input())
    area_rectangle = rectangle_side1 * rectangle_side2
    print("{0:.3f}".format(area_rectangle))
if figure_type == "circle":
    radius = float(input())
    area_circle = radius * radius * math.pi
    print("{0:.3f}".format(area_circle))
if figure_type == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    area_triangle = (triangle_height * triangle_side)/2
    print("{0:.3f}".format(area_triangle))
