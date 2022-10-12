text = input()
new_text = ""
current_text = ''
for index in range(len(text)):
    if not text[index].isnumeric():
        current_text += text[index]
    else:
        number_to_multiply = ''
        for ch_to_check in range(index, len(text)):
            if text[ch_to_check].isnumeric():
                number_to_multiply += text[ch_to_check]
            else:
                break
        current_text = current_text * int(number_to_multiply)
        new_text += current_text
        current_text = ''

print(f"Unique symbols used: {len(set(new_text.upper()))}")
print(new_text.upper())
