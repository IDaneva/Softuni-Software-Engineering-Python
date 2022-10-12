characters = input().split(", ")
ascii_dict = {characters[i]: int(ord(characters[i])) for i in range(0, len(characters))}
print(ascii_dict)