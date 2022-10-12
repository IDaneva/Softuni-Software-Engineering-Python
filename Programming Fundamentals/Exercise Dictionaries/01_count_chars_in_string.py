text = input().replace(" ", "")
symbol_dict = {}
for ch in text:
    if ch not in symbol_dict:
        symbol_dict[ch] = 0
    symbol_dict[ch] += 1

for key, value in symbol_dict.items():
    print(f"{key} -> {value}")
