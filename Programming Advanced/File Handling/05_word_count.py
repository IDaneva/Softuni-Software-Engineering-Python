words = {}

words_to_search_file = open("words.txt", "r")

for whole_sentence in words_to_search_file:
    for word in whole_sentence.split():
        words[word] = 0

words_to_search_file.close()

with open('input.txt') as file:
    for line in file:
        for searched in words:
            if searched in line.lower():
                words[searched] += 1

print(words)
words = sorted(words.items(), key=lambda x: -x[1])
print(words)

output = open('output.txt', "a")
for w, times in words:
    output.write(f"{w}-{times} \n")
