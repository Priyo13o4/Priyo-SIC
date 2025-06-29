def rajunkunte() :
    print("We came to our college")

def yelahanka():
    name = "Priyodip" #name(reference) is in the stack area , the objects are in heap area 
    print("We came to get the textbooks from the stall")
    rajunkunte()
    print("We came back to have our lunch with ",name)

def Hebbal () :
    print("We came to the biggest new mall of bengaluru")
    yelahanka()
    print("We Came back to attend interview for internship at bell")


print("I am at home ")
Hebbal()
print("I came back to home")