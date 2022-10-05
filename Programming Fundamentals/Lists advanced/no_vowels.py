text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

text_without_vowels = [ch for ch in text.lower() if ch not in vowels]
print("".join(text_without_vowels))
