from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
paper_size = deque([int(x) for x in input().split(", ")])

filled_boxes = 0

while True:
    if not eggs or not paper_size:
        break
    first_egg = eggs.popleft()
    last_piece_of_paper = paper_size.pop()

    if first_egg <= 0:
        paper_size.append(last_piece_of_paper)
        continue

    if first_egg == 13:
        first_piece = paper_size.popleft()
        paper_size.append(first_piece)
        paper_size.appendleft(last_piece_of_paper)
        continue

    if first_egg + last_piece_of_paper <= 50:
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")


if eggs:
    print(f"Eggs left: {', '.join(list(map(str, eggs)))}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(list(map(str, paper_size)))}")
