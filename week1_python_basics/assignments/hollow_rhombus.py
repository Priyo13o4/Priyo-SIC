height = int(input("please enter the height of the rhombus :"))

for i in range(height) :
    print ("  "*(height-i-1),end = '')
    for j in range(height):
        if i == 0 or i == height - 1 or j == 0 or j == height - 1 :
            print("* ",end = '')
        else:
            print( "  ",end = '')
    print()