def rectangle(length, width):
    def area():
        rec_area = length * width
        return rec_area

    def perimeter():
        rec_per = 2 * length + 2 * width
        return rec_per

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    result = f"Rectangle area: {area()}" + "\n" + f"Rectangle perimeter: {perimeter()}"
    return result

print(rectangle(2, 10))
print(rectangle('2', 10))