exploding_text = [ch for ch in input()]

explosion = 0
new_text = []
for index in range(len(exploding_text)):
    if explosion > 0 and exploding_text[index] != ">":
        explosion -= 1
    elif exploding_text[index] == ">":
        explosion += int(exploding_text[index + 1])
        new_text.append(exploding_text[index])
    else:
        new_text.append(exploding_text[index])

print("".join(new_text))
