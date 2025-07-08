numbers = (input("Enter the numbers : ")).split()
X = int(input("enter x"))
sorted1 = sorted(numbers)
print(sorted1)
Y = sorted1[:X]
x = int(Y[-1])
p = sorted1(x) - sorted1(x-1) - 1
print(p)