import string

all_lines = []
row = 1
with open("text2.txt") as file:
    for line in file:
        punctuation = 0
        letters = 0
        for ch in line:
            if ch in string.punctuation:
                punctuation += 1
            elif ch.isalpha():
                letters += 1
        print(f"Line {row}: {line.strip()} ({letters})({punctuation})")
        row += 1
