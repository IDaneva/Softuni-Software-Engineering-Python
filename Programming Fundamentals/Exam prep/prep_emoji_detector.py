import re

cool_threshold = 1
text = input()
search_pattern_for_emojis = r"(\:{2}|\*{2})([A-Z][a-z]{2,})\1"
search_pattern_for_digits= r"\d"
digit_result = re.finditer(search_pattern_for_digits, text)
emoji_result = re.finditer(search_pattern_for_emojis, text)
found_emojis = 0
cool_emojis = []

for match in digit_result:
    cool_threshold *= int(match.group())
print(f"Cool threshold: {cool_threshold}")

for emoji_match in emoji_result:
    found_emojis += 1
    current_coolness = 0
    for ch in emoji_match.group(2):
        current_coolness += ord(ch)
    if current_coolness >= cool_threshold:
        cool_emojis.append(f"{emoji_match.group(1)}{emoji_match.group(2)}{emoji_match.group(1)}")

print(f"{found_emojis} emojis found in the text. The cool ones are:")
for em in cool_emojis:
    print(em)
