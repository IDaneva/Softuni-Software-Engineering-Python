# while True:
#     number = float(input())
#
#     if number >= 1 and number <= 100:
#         condition = False
#         print(f"The number {number:.1f} is between 1 and 100")
#         break


number = float(input())

while number < 1 or number > 100:
    number = float(input())
else:
    print(f"The number {number:.1f} is between 1 and 100")
