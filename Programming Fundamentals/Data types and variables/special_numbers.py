number = int(input())

for i in range(1, number + 1):
    all_chisla = str(i)
    if len(str(i)) == 1:
        if i == 5 or i == 7 or i == 11:
            print(f"{i} -> True")
        else:
            print(f"{i} -> False")
    elif len(str(i)) == 2:
        if int(all_chisla[0]) + int(all_chisla[1]) == 5 or int(all_chisla[0]) + int(all_chisla[1]) == 7 or int(all_chisla[0]) + int(all_chisla[1]) == 11:
            print(f"{i} -> True")
        else:
            print(f"{i} -> False")
    elif len(str(i)) == 3:
        if int(all_chisla[0]) + int(all_chisla[1]) + int(all_chisla[2]) == 5 or int(all_chisla[0]) + int(all_chisla[1]) + int(all_chisla[2]) == 7 or int(n[0]) + int(n[1]) + int(all_chisla[2])== 11:
            print(f"{i} -> True")
        else:
            print(f"{i} -> False")
    elif len(str(i)) == 4:
        if int(all_chisla[0]) + int(all_chisla[1]) + int(all_chisla[2]) == 5 or int(all_chisla[0]) + int(all_chisla[1]) + int(all_chisla[2]) == 7 or int(n[0]) + int(n[1]) + int(all_chisla[2]) == 11:
            print(f"{i} -> True")
        else:
            print(f"{i} -> False")







# number = int(input())
#
# for num in range(1, number + 1):
#     sum_of_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits/10)
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")

