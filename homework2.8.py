data = ["5", 0, "3", True, "", 2, "x", False]
total = 0

for item in data:
    if type(item) == str and item.isdigit():
        total += int(item)
    elif type(item) == int and type(item) != bool:
        total += item

print("Total:", total)