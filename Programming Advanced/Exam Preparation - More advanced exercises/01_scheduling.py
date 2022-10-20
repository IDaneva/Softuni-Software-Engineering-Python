from collections import deque

jobs = [int(x) for x in input().split(", ")]
interested_index = int(input())


sorted_jobs = deque(sorted(jobs))
made_cycles = 0

for num in sorted_jobs:
    found_index = jobs.index(num)
    made_cycles += jobs[found_index]
    jobs[found_index] = "x"
    if found_index == interested_index:
        break

print(made_cycles)
