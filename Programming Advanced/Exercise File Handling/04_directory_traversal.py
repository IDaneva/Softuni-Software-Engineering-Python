import os

all_files = os.listdir(input("Enter directory path: "))
file_dict = {}

for current_file in all_files:
    name, extension = current_file.split(".")
    if extension not in file_dict:
        file_dict[extension] = []
    file_dict[extension].append(name)

report = ""

result = dict(sorted(file_dict.items(), key=lambda x: (x[0], x[1])))

for ext, files in result.items():
    report += f".{ext}\n"
    for current in files:
        report += f"--- {current}\n"

with open("report.txt", "w") as f:
    f.write(report)
