def loading_bar(number):
    if number == 100:
        print("100% Complete! \n [%%%%%%%%%%]")
    else:
        percents = number//10 * "%"
        dots = (10 - number//10) * "."
        print(f"{number}% [{percents}{dots}]")
        print("Still loading...")


number = int(input())
loading_bar(number)