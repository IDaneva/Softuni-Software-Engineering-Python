# import math
#
# max_points = 0
# powerful_word = ""
#
# while True:
#     word = input()
#
#     if word == "End of words":
#         break
#     else:
#         points = 0
#         for ch in word:
#             points += ord(ch)
#             if ch[0] in "a e i o u y A E I O U Y ":
#                 points *= len(word)
#             else:
#                 points = math.floor(points / len(word))
#
#             if points > max_points:
#                 max_points = points
#                 powerful_word = word
#
# print(f"The most powerful word is {powerful_word} - {max_points}" )


import math

max_points = 0
powerful_word = ""
condition = False

while True:
    word = input()

    if word == "End of words":
        break
    else:
        points = 0
        condition = False

        for index, digit in enumerate(word):
            points += ord(digit)
            if index == 0 and digit in "a e i o u y A E I O U Y ":
                condition = True
        if condition:
            points *= len(word)
        else:
            points = math.floor(points / len(word))

        if points > max_points:
            max_points = points
            powerful_word = word

print(f"The most powerful word is {powerful_word} - {max_points}")