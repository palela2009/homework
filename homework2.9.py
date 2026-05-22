transactions = {
    "გიო": "100",
    "ნიკა": 50,
    "აკაკი": "30a",
    "ლევანი": 0,
    "ანა": "70",
    "მარი": True
}
total = 0

for val in transactions.values():
    if type(val) == str and val.isdigit():
        total += int(val)
    elif type(val) == int and type(val) != bool:
        total += val
    elif type(val) == bool and val == True:
        total += int(val)

print("Total:", total)