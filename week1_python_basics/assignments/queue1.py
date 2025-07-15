#Queue with insertion in front and deletion from back
import sys
def en_queue() : 
    ele = input()
    queue.append(ele)
    print(f"element {ele} inserted")
    

def de_queue() :
    if len(queue) == 0 :
        print("The queue is empty")
    else :
        del queue[0] 
        return (f"element removed from the queue")

def display_queue() : 
    if len(queue) == 0 :
        print("The queue is empty")
    else :
        print(queue)

def exit_program() :
    print("Program exited")
    sys.exit(0)

def invalid_choice() : 
    print("Invalid Choice")

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
    choice = int(input("Your Choice please : "))
    menu(choice)

        
