words_in_morse_to_translate = input().split(" | ")

translated_message = []
morse_alphabet = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
                  "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
                  "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
                  ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
                  "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"}
for word in words_in_morse_to_translate:
    current_word = ""
    for letter in word.split():
        if letter in morse_alphabet:
            current_word += morse_alphabet[letter]
    translated_message.append(current_word)

print(' '.join(translated_message).upper())
