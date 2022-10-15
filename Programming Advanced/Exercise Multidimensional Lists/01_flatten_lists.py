numbers = input().split("|")

result = [x.split() for x in numbers[::-1]]

print(' '.join([" ".join(row) for row in result]))

# subs = []
#
# for s in numbers[::-1]:
#     subs.extend(s.split())
# print(*subs)
