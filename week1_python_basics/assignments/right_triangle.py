#print a right angled triangle for a given height
height = int(input("Please enter the height of the triangle : "))
for i in range(1,height+1) :
    for k in range (1 , i +1) :
        print("*",end = '')
    print()