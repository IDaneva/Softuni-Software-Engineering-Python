box_of_clothes_stack = [int(s) for s in input().split()]
capacity_for_one_rack = int(input())
current_capacity = capacity_for_one_rack
filled_racks = 1

while box_of_clothes_stack:
    last_piece = box_of_clothes_stack[-1]
    if current_capacity - last_piece < 0:
        filled_racks += 1
        current_capacity = capacity_for_one_rack
        current_capacity -= last_piece
        box_of_clothes_stack.pop()
    else:
        current_capacity -= last_piece
        box_of_clothes_stack.pop()
print(filled_racks)
