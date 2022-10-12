import re

search_pattern = r"((www)\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"
validated = []

while True:
    text = input()
    if not text:
        break

    matches = re.search(search_pattern, text)
    if matches:
        validated.append(matches.group(0))

for url in validated:
    print(url)
