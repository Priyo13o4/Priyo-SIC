def isSameReflection() : 
    original_str = input("Please enter the original string : ")
    rotated_str = input("Please enter the rotated string :")

    temp = original_str * 2

    if rotated_str in temp :
        return 1
    elif rotated_str > original_str or original_str < rotated_str :
        return "Invalid input, String lengths dont match"
    else :
        return -1
    

print(isSameReflection())

#We can also solve this by index slicing