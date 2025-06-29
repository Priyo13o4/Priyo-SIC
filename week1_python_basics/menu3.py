import sys as s
def ice_cream():
    print("Yummy Amul icecream")
    
def chats() : 
    print("Spicy Masala Puri")

def milk_shake() :
    print('Chocolate milkshake')

def junk() :
    print('Lot of Pepsi and Kurkure')

def exit_program() :
    s.exit("End of Program")

def invalid_choice() :
    print("Invalid choice Number")

def menu(choice) :
    match(choice) :
        case 1 : ice_cream() 
        case 2 : chats() 
        case 3 : milk_shake() 
        case 4 : junk() 
        case 5 : exit_program ()
        case _: invalid_choice() #default case

while True :
    print('1:IceCream 2:Chats 3:Milkshake 4:Junk 5:Exit')
    choice = int(input('Your Choice please :'))
    menu(choice)