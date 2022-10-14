first_sequence = {*set(input().split())}
second_sequence = {*set(input().split())}

N = int(input())

for _ in range(N):
    command = input().split()
    numbers = command[2::]
    instructions = " ".join(command[:2])

    if instructions == "Add First":
        for n in numbers:
            first_sequence.add(n)
    elif instructions == "Add Second":
        for n in numbers:
            second_sequence.add(n)
    elif instructions == "Remove First":
        for num in numbers:
            if num in first_sequence:
                first_sequence.remove(num)
    elif instructions == "Remove Second":
        for num in numbers:
            if num in second_sequence:
                second_sequence.remove(num)
    elif instructions == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

first_sequence = sorted(list(map(int, first_sequence)))
second_sequence = sorted(list(map(int, second_sequence)))

print(", ".join(list(map(str, first_sequence))))
print(", ".join(list(map(str, second_sequence))))
