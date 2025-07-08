import sys as s 
def push() :
    stack.append(input())
    print()
def pop() :
    if len(stack) == 0 :
        print("Stack is empty")
        return
    else : 
        stack.pop()

def display() :
    if len(stack) == 0 :
        print("Stack is empty")
        return
    else :
        print("The stack elements are : ",stack[::-1])

def exit_program() :
    print("End of Program")
    s.exit(0)

def invalid_choice() :
    print("Invalid choice Number")

stack = []
def menu(choice) :
    match(choice) :
        case 1 : push() 
        case 2 : pop() 
        case 3 : display() 
        case 4 : exit_program ()
        case _: invalid_choice() #default case
while True :
    print('Your choice are 1:push 2:pop 3:display 4:Exit')
    choice = int(input('Your Choice please :'))
    menu(choice)
