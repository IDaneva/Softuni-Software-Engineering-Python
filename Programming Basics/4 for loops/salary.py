open_tabs = int(input())
salary = int(input())

condition = False

for _ in range(open_tabs):
    current_website = input()
    if current_website == "Facebook":
        salary -= 150
    elif current_website == "Instagram":
        salary -= 100
    elif current_website == "Reddit":
        salary -= 50

    if salary <= 0:
        condition = True
        break

if not condition:
    print(salary)
else:
    print("You have lost your salary.")
