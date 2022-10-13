from collections import deque

kids = deque(input().split())
number_of_tosses = int(input())
current_num = 1
while len(kids) > 1:
    kid = kids.popleft()
    if current_num == number_of_tosses:
        print(f"Removed {kid}")
        current_num = 1
    else:
        kids.append(kid)
        current_num += 1
print(f"Last is {''.join(kids)}")
