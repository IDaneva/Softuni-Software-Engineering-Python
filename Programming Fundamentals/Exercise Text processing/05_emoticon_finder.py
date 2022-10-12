found_emoticons = []

text = input()

for index in range(0, len(text)):
    if text[index] == ":":
        found_emoticons += text[index] + text[index + 1]
    else:
        continue

for ch in range(0, len(found_emoticons), 2):
    print(f"{found_emoticons[ch]}{found_emoticons[ch+1]}")