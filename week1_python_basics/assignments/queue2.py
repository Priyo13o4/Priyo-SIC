import sys as s
def en_queue():
    ele = input()
    queue.insert(0,ele)
    print()
    
def de_queue () : 
    if len(queue) == 0 :
        print(' Queue is empty')
        return
    print(f"The eleemnt {queue[-1]} is deleted")
    del queue[-1]
    
def display_queue() : 
    if len(queue) == 0 :
        print(' Queue is empty')
        return
    print('Queue elements are :' , queue [::-1])

def exit_program() :
    s.exit("End of Program")

def invalid_choice() :
    print("Invalid choice Number")

queue = []
def menu(choice) :
    match(choice) :
        case 1 : en_queue() 
        case 2 : de_queue() 
        case 3 : display_queue() 
        case 4 : exit_program ()
        case _: invalid_choice() #default case

while True :
    print('Your choice are 1:Insert 2:pop 3:display 4:Exit')
    choice = int(input('Your Choice please :'))
    menu(choice)