def function(ch1, ch2):
    all_characters_inbetween = []
    for current_char in range(ord(ch1) + 1, ord(ch2)):
        all_characters_inbetween.append(chr(current_char))

    return all_characters_inbetween


character1 = input()
character2 = input()

result = function(character1, character2)
print(" ".join(result))
