current_version = input().replace(".", "")
new_version = str(int(current_version) + 1)
new_list = []
for ch in new_version:
    new_list.append(ch)
print(".".join(new_list))
