with open("example_file.txt", 'r', encoding="utf-8") as f:
    lines = f.read()

print(lines)
lines = lines.replace("linia", "CHANGED")
print("-------------------------------")
print(lines)

with open("example_file.txt", 'w', encoding="utf-8") as f:
    f.write(lines)
