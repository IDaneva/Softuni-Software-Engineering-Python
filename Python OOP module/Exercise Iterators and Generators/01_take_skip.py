class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.counter = 0
        self.num = -self.step

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter == self.count:
            raise StopIteration

        self.counter += 1
        self.num += self.step
        return self.num


numbers = take_skip(10, 5)

for number in numbers:

    print(number)