number_of_lines = int(input())
longest_intersection = []

for row in range(number_of_lines):
    range1, range2 = input().split("-")
    start1, end1 = range1.split(",")
    start2, end2 = range2.split(",")
    set1 = {s for s in range(int(start1), int(end1) + 1)}
    set2 = {s for s in range(int(start2), int(end2) + 1)}
    if len(set1.intersection(set2)) > len(longest_intersection):
        longest_intersection = set1.intersection(set2)

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
