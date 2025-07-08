def my_function(param1 =1,param2=2) : #default arguements
    print(f"num1 = {param1} ,num2 = {param2}")
    return param1+param2
num1 = 3
num2 = 4
result = my_function()
print("results = ",result)

result = my_function(num1)
print(f"num1 = {num1} ,num2 = {num2}")
print("results = ",result)
result = my_function(num1,num2)