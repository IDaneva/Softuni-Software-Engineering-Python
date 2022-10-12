import re

search_pattern = r"\d+"

while True:
    text = input()

    if not text:
        break
    matches = re.findall(search_pattern, text)
    if matches:
        print(" ".join(matches), end=" ")
