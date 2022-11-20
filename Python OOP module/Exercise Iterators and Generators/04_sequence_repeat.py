class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.used_characters = -1
        if len(sequence) < self.number:
            self.sequence *= self.number

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.used_characters += 1

        if self.used_characters == self.number:
            raise StopIteration

        character = self.sequence[self.index]
        return character


result = sequence_repeat('I Love Python', 3)

for item in result:

    print(item, end ='')