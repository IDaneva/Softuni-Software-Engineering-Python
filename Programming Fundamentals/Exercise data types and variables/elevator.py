import math

number_of_people = int(input())
elevator_capacity = int(input())

courses = number_of_people/elevator_capacity
print(math.ceil(courses))