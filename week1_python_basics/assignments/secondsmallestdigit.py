#Find 2nd smallest digit in a number

input_number = (input("Please enter the Number :"))
sorted_input = sorted(input_number)
smallest_digit = sorted_input[0]

for i in range (len(sorted_input) ):
    if int(smallest_digit) < int(sorted_input[i]):
        second_smallest_digit = sorted_input[i]
        break
    else : 
        second_smallest_digit = smallest_digit
        
print("The Second Smallest Number is :",second_smallest_digit)

        
