#Building a custom range function 
def my_range (*args) :
    i = 1
    while i < len(args) :
        if type[args[i]] is not int :
            raise TypeError
        i += 1

    if len(args) == 0 or len(args) > 3 :
        raise TypeError
    if len(args) == 1 :
        i = 0
        while i<args[0]:
            yield i 
            i+=1
    elif len(args) == 2 :
        i = args[0]
        while i <args[1]:
            yield i
            i+=1 
    elif len(args) == 3 :
        if args[2] == 0 :
            raise ValueError
    elif len(args) == 3 and args[2] > 0:
        i = args[0]
        while i <args[1]:
            yield i
            i += args[2]
    else : 
        i = args[0]
        while i >args [1] :
            yield i
            i+= args[2]

number_of_lines = int(input("Enter number of lines of the Square: "))
for i in my_range(number_of_lines):
        print('@ ' * number_of_lines)
