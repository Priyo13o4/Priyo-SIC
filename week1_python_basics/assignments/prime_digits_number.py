#Find the Count number of Prime digits in a number

input_number = (input("Please Enter the Nummber : "))
count = 0
for i in input_number : 
    temp = int(i)
    if temp in [2,3,5,7] :
        count += 1
            
print("Number of prime digits are : ", count)

