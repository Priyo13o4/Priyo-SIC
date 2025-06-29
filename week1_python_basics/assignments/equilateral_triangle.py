lines = int(input("Please enter height of the traingle : "))

for i in range(1,lines+1):
    for j in range(i,lines) :
        print(" ",end = '')
    for k in range(1,(2*i)) :
        print("*",end = '')
    print("")
    