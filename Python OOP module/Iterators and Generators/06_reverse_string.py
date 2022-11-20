def reverse_text(text):
    text = list(text)
    while text[::-1]:
        yield text.pop()


for char in reverse_text("step"):
    print(char, end='')