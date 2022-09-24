starting_num = input()
ending_num = input()


for digit1 in range(int(starting_num[0]), int(ending_num[0]) + 1):
    for digit2 in range(int(starting_num[1]), int(ending_num[1]) + 1):
        for digit3 in range(int(starting_num[2]), int(ending_num[2]) + 1):
            for digit4 in range(int(starting_num[3]), int(ending_num[3]) + 1):
                if digit1 % 2 != 0 and digit2 % 2 != 0 and digit3 % 2 != 0 and digit4 % 2 != 0:
                    print(f"{digit1}{digit2}{digit3}{digit4}", end=" ")





# for num1 in range(1, 10):
#     for num2 in range(1, 10):
#         for num3 in range(1, 10):
#             for num4 in range(1, 10):
#                 if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
#                     print(f"{num1}{num2}{num3}{num4}", end=" ")
