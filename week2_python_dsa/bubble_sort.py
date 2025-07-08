def bubble_sort(input_list):
    n = len(input_list)

    for i in range(n-1) :
        swapped = False
        for j in range(n-i-1) :
            if input_list[j] > input_list [j+1] :
                input_list[j],input_list[j+1] = input_list[j+1] , input_list[j]
                swapped = True
            
        if not swapped : 
            break

    return input_list

list = [int(x) for x in input("Please eneter the numbers :").split()]
print(bubble_sort(list))



