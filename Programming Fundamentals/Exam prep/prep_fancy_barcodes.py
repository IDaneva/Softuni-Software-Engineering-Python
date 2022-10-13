import re

count_of_barcodes = int(input())
barcode_search_pattern = r"\@#{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])\@#+"
for _ in range(count_of_barcodes):
    barcode = input()
    result = re.findall(barcode_search_pattern, barcode)
    if result:
        group = ""
        for ch in result[0]:
            if ch.isdigit():
                group += ch
        if group == "":
            print("Product group: 00")
        else:
            print(f"Product group: {group}")
    else:
        print("Invalid barcode")

