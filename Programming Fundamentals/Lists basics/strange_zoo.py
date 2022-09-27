tail = input()
body = input()
head = input()

animals_list = [tail, body, head]

animals_list[0], animals_list[2] = animals_list[2], animals_list[0]
print(animals_list)