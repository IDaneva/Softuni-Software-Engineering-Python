class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.dictionary) -1:
            raise StopIteration

        info = list(self.dictionary.items())
        self.counter += 1
        return info[self.counter]


result = dictionary_iter({"name": "Peter", "age": 24})

for x in result:
    print(x)