class vowels:
    VOWELS = "AEOUIYaeiouy"

    def __init__(self, text):
        self.text = text
        self.found_vowels = [ch for ch in self.text if ch in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.found_vowels:
            raise StopIteration

        return self.found_vowels.pop(0)


my_string = vowels('Abcedifuty0o')

for char in my_string:

    print(char)
