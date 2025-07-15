#program1.py

import numpy as np
import scipy as sp


array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array) # Average
median = np.median(array) # mid value in the list
mode   = sp.stats.mode(array) # most most occuring element in the list

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode Occurances = ', mode.count)
print(f'Mode Count = ', len(mode.count))
#--------------------------------
#program2.py

#import numpy as np

array1 = np.array([[1, 2], [3, 4]]) 
array2 = np.array([[1, 2], [3, 4]]) 

print(array1 == array2) # Does element wise comparison and returns truth value for every comparison which is again stored in the respective sized np array

comparison = (array1 == array2)
equal_arrays = comparison.all() # Here all the truth values of the inferred np array is taken and if all are True then it returns True, else False.

print(equal_arrays)
#--------------------------------
#program3.py

#import numpy as np

# Problem1: Finding indices where spendings are greater than 100

# Explanation: Using np.where() to find indices where the condition is met

# week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
# high_spend = np.where(spendings > 100)
# print(high_spenders) # Output: Indices where the values are greater than 100
#--------------------------------
#program4.py
# In a np array of spendings of the week, find the highest spending.


# import numpy as np
week_spendings = np.array([50,120,30,40,200,90,300])
highest_spending = max(week_spendings)
print(highest_spending)


#-------------------------------------------------------
#program5.py
# In a np array of spendings of the week, find the highest spending and the day.

week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
index = 1
big_spending = week_spendings[0]
index = np.argmax(week_spendings)
days = {1:'mon', 2:'tue', 3:'wed', 4:'thus', 5:'fri', 6:'sat', 7:'sun'}
print(big_spending, days[index])

'''
for i in range(len(week_spendings)):
	if week_spendings[i] > big_spending:
		big_spending = week_spendings[i]
		index = i
'''
#-------------------------------------------------------
# Program7.py

#Generating random floating-point numbers between 0 and 1

# Explanation: Using np.random.rand() to create a random array of given shape

random_data = np.random.rand(3, 4) # Creates a 3x4 array with random values
print(random_data)

# -------------------------------------------------------
# program8.py

import math

user_number = int(input('Enter a number of your choice between [0 and 9]: '))
system_number = math.random(10)
if system_number == user_number:
	print('CrorePati')
else:
	print('RoadPati')
