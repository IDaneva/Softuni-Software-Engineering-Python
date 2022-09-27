number_of_lines = int(input())
word = input()
list_of_words = []
filtered_list = []
for _ in range(number_of_lines):
    current_text = input()
    list_of_words.append(current_text)
print(list_of_words)

for item in list_of_words:
    if word in item:
        filtered_list.append(item)
print(filtered_list)