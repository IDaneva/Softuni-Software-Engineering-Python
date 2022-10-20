from collections import deque

flower_dict = {
    "rose": ["r", "o", "s", "e"],
    "tulip": ["t", "u", "l", "i", "p"],
    "lotus": ["l", "o", "t", "u", "s"],
    "daffodil": ["d", "a", "f", "f", "o", "d", "i", "l"]
}

vowels = deque(input().split())
consonants = input().split()

found_word = []

success = False

while not success:
    if not vowels or not consonants:
        break
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    for flower in flower_dict:
        if first_vowel in flower_dict[flower]:
            flower_dict[flower] = [x for x in flower_dict[flower] if x != first_vowel]

        if last_consonant in flower_dict[flower]:
            flower_dict[flower] = [x for x in flower_dict[flower] if x != last_consonant]

        if not flower_dict[flower]:
            found_word = flower
            success = True
            break

if success:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
