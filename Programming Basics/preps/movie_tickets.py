a1 = int(input())
a2 = int(input())
n = int(input())

for code in range(a1, a2 - 1):
    symbol1 = chr(code)
    for symbol2 in range(1, n - 1):
        for symbol3 in range(1, int((n / 2)) -1):
            symbol4 = ord(symbol1)
            print(f"{symbol1}{symbol2}{symbol3}{symbol4}")
