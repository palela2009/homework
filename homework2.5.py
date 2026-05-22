mylist = range(100)

i = 0


while i < len(mylist):
    number = mylist[i]

    square = number ** 2
    cube = number ** 3


    print(f"რიცხვი: {number}  კვადრატი (x²): {square}  კუბი (x³): {cube}")

    i += 1