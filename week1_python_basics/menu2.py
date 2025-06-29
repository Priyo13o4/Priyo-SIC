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

menu = { #not calling the function
        1 : ice_cream ,
        2 : chats ,
        3 : milk_shake ,
        4 : junk ,
        5 : exit_program 
    }
while True :
    print('1:IceCream 2:Chats 3:Milkshake 4:Junk 5:Exit')
    choice = int(input('Your Choice please :'))
    menu.get(choice,invalid_choice)() #Making a fucntion call here 