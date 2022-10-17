with open("text.txt", "r") as file:
    all_text = file.readlines()

all_filtered_text = [all_text[i].strip() for i in range(0, len(all_text), 2)]

symbols = ["-", ",", ".", "!", "?"]
result = []
for current_line in all_filtered_text:
    for symbol in symbols:
        current_line = current_line.replace(symbol, "@")
    result.append(current_line.split())

for text in result:
    print(*text[::-1])
