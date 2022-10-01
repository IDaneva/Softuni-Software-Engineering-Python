text = input()

list_of_indexes = []

for i in range(len(text)):
    if text[i].isupper():
        list_of_indexes.append(i)
    else:
        continue
print(list_of_indexes)

