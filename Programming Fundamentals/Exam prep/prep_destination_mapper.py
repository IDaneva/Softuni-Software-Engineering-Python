import re

places_on_map = input()
search_pattern_for_places = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
result = re.finditer(search_pattern_for_places, places_on_map)

total_points = 0
destinations = []
for match in result:
    total_points += len(match.group(2))
    destinations.append(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_points}")
