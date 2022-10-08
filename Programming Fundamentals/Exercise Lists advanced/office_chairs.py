number_of_rooms = int(input())
free_chairs = True
number_of_free_chairs = 0

for current_room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    chairs_in_room = len(chairs_and_visitors[0])
    visitors_in_room = int(chairs_and_visitors[1])
    if chairs_in_room < visitors_in_room:
        print(f"{visitors_in_room - chairs_in_room} more chairs needed in room {current_room}")
        free_chairs = False
    else:
        number_of_free_chairs += chairs_in_room - visitors_in_room

if free_chairs:
    print(f"Game On, {number_of_free_chairs} free chairs left")
