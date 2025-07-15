input_list = list(map(int,input("Please enter the List :").split()))
check_frequency_of = int(input("Please enter the element for which to find freqeuncy : "))
frequency = 0
if check_frequency_of not in input_list : 
    print("element not in list")
else :
    for i in range (len(input_list)) :
        if check_frequency_of == input_list[i] :
            frequency += 1

    print(f"The frequency of element {check_frequency_of} is {frequency}")
