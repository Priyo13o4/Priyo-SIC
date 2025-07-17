import numpy as np

a1 = np.zeros(3)
a2 = np.zeros((1,4))
a3 = np.zeros((2,5))

print(type(a1))
print(type(a2))
print(type(a1[0]))
print(type(a2[0][3]))

a1 = np.full((2,4),5)
print(a1) #Two rows of 4 elements , all being 5 
a2 = np.full((1,5),10,int)
print(a2)
print(type(a2[0][2]))

#-----------------------------------------------------------------------------------------------------------------------------
# arange()

array1 = np.arange(10)
array2 = np.arange(10, 20)
array3 = np.arange(10, 30, 3)

print(type(array1))
print(array1)
print(array2)
print(array3)

#-----------------------------------------------------------------------------------------------------------------------------

# ones()

array1 = np.ones(10)
array2 = np.ones((2, 8))
array3 = np.ones((3, 5))

print(type(array1))
print(array1)
print(array2)
print(array3)

#-----------------------------------------------------------------------------------------------------------------------------
vector = np.arange(5)
print('Vector shape:', vector.shape) #1D array

matrix = np.ones([3, 2])
print('Matrix:', matrix) #2D array
print('Matrix shape:', matrix.shape)

tensor = np.zeros([2, 3, 3])
print('Tensor:', tensor) #3D array
print("Tensor shape:", tensor.shape) #Stacking matrices on top of the other
#-----------------------------------------------------------------------------------------------------------------------------
arr = np.arange(1, 10)
print(arr, '\n')

# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n')

# Reshape back to the original size
arr = arr.reshape(9)
print(arr)

# arr = arr.reshape(2, 5) # ValueError
# print(arr)
#-----------------------------------------------------------------------------------------------------------------------------

arr1 = np.arange(12)

arr2 = arr1.reshape(2, 6)
arr3 = arr1.reshape(6, 2)
arr4 = arr1.reshape(3, 4)
arr5 = arr1.reshape(12, 1)
arr6 = arr1.reshape(4, 3)

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)

#-----------------------------------------------------------------------------------------------------------------------------

arr = np.arange(1, 10).reshape(3, -1) # Here python infers/decides the number of columns by itself. This is called as method chaining
print(arr)