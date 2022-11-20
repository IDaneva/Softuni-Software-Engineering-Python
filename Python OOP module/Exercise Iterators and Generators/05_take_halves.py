def solution():

    def integers():
        num = 1
        while num:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        nums = []
        for _ in range(n):
            nums.append(next(seq))

        return nums

    return (take, halves, integers)


take = solution()[0]

halves = solution()[1]

print(take(5, halves()))
