# Print the Prime numbers in decreasing order between m and n (m < n)

print("Prints the prime numbers in decreasing order from between m and n ")
input_start = int(input("Please enter the starting number (m) :" ))
input_end = int(input("Please enter the ending number (n) :"))
if input_start > input_end :
     print ("Invalid input , starting number cannot be greater than ending number")
else :  
    for i in range (input_end-1,input_start,-1) : 
        is_prime = True
        for k in range (2,i//+2) :
            if i%k == 0 :
                is_prime = False
                break
        if is_prime:
            print(i, end = ',')
        

