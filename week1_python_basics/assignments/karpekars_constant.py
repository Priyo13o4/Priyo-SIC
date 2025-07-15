#Accept A number from the user(4-digit number , where the digit can repeat atmost two times) and print the count of recursions required to arrive at Karpekar's constant.
'''-> What is Karpekar's Constant 
steps :
1. take a 4 digit number : 6931
2. Decreasing order : 9631
3. Increasing Order : 1369 
4. difference : 8262 
	-> keep repeating : 8622 , 2268 : 6354
						6543 , 3456 : 3087
						8730 , 0378 : 8352
						8532 , 2358 : 6174 
						7641 , 1467 : 6174 ---- > Karpekar's Constant'''
def get_sorted_numbers(number):

    num_str = str(number)
    asc = int("".join(sorted(num_str)))     
    desc = int("".join(sorted(num_str, reverse=True))) 

    return desc, asc 

def recursion_number(number):
    count = 0
    while True:
        desc, asc = get_sorted_numbers(number)
        diff = desc - asc
        count += 1
        if diff == 6174:
            break
        elif diff == 0:
            print("All digits are same. Kaprekar process not possible.")
            return
        number = diff
    print("Kaprekar's constant reached in", count, "iterations.")

# Input from user
number = input("Please enter a 4-digit number: ")

if len(number) != 4:
    print("Invalid input. Please enter exactly a 4-digit number.")
else:
    recursion_number(int(number))

    
