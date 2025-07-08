input_list = [int(x) for x in input("Enter the numbers: ").split()]
search_num = 19
sorted_input=sorted(input_list)
low = 0 
high = len(sorted_input) - 1

while high>=low :
    mid = (low + high) // 2

    if sorted_input[mid] == search_num :
        print(f"Element found at index {mid}")
        break
    elif sorted_input[mid] < search_num :
        low = mid + 1
    else :
        high = mid - 1
else : 
    print("Element Not found")
        
    