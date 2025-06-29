choice = 0

menu = {
        1 : ({'Yummy Amul icecream'}),
        2 : ({'Spicy Masala Puri'}),
        4 : ({'Chocolate Milkshake'}),
        3 : ({'Lot of Pepsi and Kurkure'}),
        5 : ({'End of Program'}),
        }
while True :
    print('1:IceCream 2:Chats 3:Milkshake 4:Junk 5:Exit')
    choice = int(input('Your Choice please :'))
    string = menu.get(choice,print('Invalid choice Number'))
    print(string)