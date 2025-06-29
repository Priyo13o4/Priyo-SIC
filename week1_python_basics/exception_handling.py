l1 =[1,2,3,4,5,6]
print(l1)
ele = 12
try : 
    l1.remove(l1)
    print("Hello")
    print(l1[8])

except ValueError as e : # child of Exception 
    print(print(f"{ele} was not found"))

except Exception as e : #this wont work if the specialized except block is after a generic block
    print("An error occuerd at runtime maybe while removing the element")

except : # generic exepct block , so any type of object will be caught 
       print(print("Some error occured")) # It returns a none too due to the outer print

try : 
    print(l1[8])

except ValueError as e : # if it was an index error , it would have entered this block as e matches the object type of the error 
    print(print(f"{ele} was not found"))

except Exception as e : #this wont work if the specialized except block is after a generic block
    print("An error occuerd at runtime maybe while finding the element")

except : # generic exepct block , so any type of object will be caught 
       print(print("Some error occured")) # It returns a none too due to the outer print

print('Normal execution continued')