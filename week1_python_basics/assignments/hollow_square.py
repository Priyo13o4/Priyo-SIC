side = int(input("please enter the side of the square :"))

for i in range(side):
    if i == 0 or i == side - 1:
        print("* " * side)
    else:
        print("* " + "  " * (side - 2) + "*")
