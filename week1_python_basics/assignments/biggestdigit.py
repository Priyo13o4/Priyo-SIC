#Find biggest digit in a number

input_number = (input("Please enter the Number :"))
biggest_digit = 0
for i in input_number :
    temp_digit = int(i) % 10 
    if temp_digit > biggest_digit :
        biggest_digit = temp_digit
print("The largest digit in the number is :",biggest_digit)

#Using Max Function 

# input_number = (input("Please enter the Number :"))
# biggest_digit = max(input_number)
# print("The largest digit in the number is :",biggest_digit)
