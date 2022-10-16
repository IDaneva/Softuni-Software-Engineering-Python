number_of_lines = int(input())
number_stack = []

for _ in range(number_of_lines):
    command = input().split()
    instructions = int(command[0])
    if instructions == 2:
        if len(number_stack) > 0:
            number_stack.pop()
        else:
            continue
    elif instructions == 3:
        if len(number_stack) > 0:
            print(max(number_stack))
    elif instructions == 4:
        if len(number_stack) > 0:
            print(min(number_stack))
    elif instructions == 1:
        num_to_push = int(command[1])
        number_stack.append(num_to_push)
    else:
        continue

reverse_stack = []
while len(number_stack) > 0:
    current_num = number_stack.pop()
    reverse_stack.append(str(current_num))

print(", ".join(reverse_stack))
