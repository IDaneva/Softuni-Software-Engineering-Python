from collections import deque

original_text = deque(input().split())
MAIN_COLORS = ["red", "yellow", "blue"]
SECONDARY_COLORS = ["orange", "purple", "green"]
found = []

while original_text:
    if len(original_text) == 1:
        substr = "".join(original_text.pop())
        if substr in MAIN_COLORS or substr in SECONDARY_COLORS:
            found.append(substr)

    else:
        first = original_text.popleft()
        last = original_text.pop()
        substr = first + last
        substr2 = last + first

        if substr in MAIN_COLORS or substr in SECONDARY_COLORS:
            found.append(substr)

        elif substr2 in MAIN_COLORS or substr2 in SECONDARY_COLORS:
            found.append(substr2)

        else:
            first = first[0:-1]
            last = last[0:-1]
            if len(first) > 0:
                original_text.insert(len(original_text)//2, first)
            if len(last) > 0:
                original_text.insert(len(original_text)//2, last)


for current_color in found:
    if current_color == "orange":
        if "red" and "yellow" not in found:
            found.remove(current_color)
    elif current_color == "purple":
        if "red" and "blue" not in found:
            found.remove(current_color)
    elif current_color == "green":
        if "blue" and "yellow" not in found:
            found.remove(current_color)

print(found)
