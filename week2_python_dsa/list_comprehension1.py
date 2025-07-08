n = int(input("Enter the number of elements of the array : "))
try :
    numbers = [float(num) for num in input().split()] #split is a method in the str class,return value of input is calling split
    print(numbers)
    #Normal execution continues if more instrcutors are present in the try block even if execption is hit 
except ValueError as e :
    print("You may have entered an invalid float number")

numbers.sort()
