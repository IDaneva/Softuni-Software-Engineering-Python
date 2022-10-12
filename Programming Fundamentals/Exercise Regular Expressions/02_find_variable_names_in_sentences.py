import re

search_pattern = r"\b_([A-Za-z0-9]+)\b"

text = input()

match = re.findall(search_pattern, text)
print(",".join(match))
