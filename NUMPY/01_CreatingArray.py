import numpy as np


#1D array
arr1 = np.array([1, 2, 3, 4, 5])

#2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

#3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr1)
print("-------------------------------------")
print(arr2)
print("-------------------------------------")
print(arr3)
print("-------------------------------------")

a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])
print(a)
print("-------------------------------------")
print(b) 
print("-------------------------------------")
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(a*b)

print("-------------------------------------")

#Array with default values : default values will be zero
#np.array(shape) : (3) for creataing 1d array of 3 element and (3,3) for createing 2d array
zero_1dArray = np.zeros(3) 
print(zero_1dArray)
print("-------------------------------------")
ones_1dArray = np.ones(3)
print(ones_1dArray)
print("-------------------------------------")
zero_2dArray = np.zeros((3,3))
print(zero_2dArray)
print("-------------------------------------")
ones_2dArray = np.ones((3,3))
print(ones_2dArray)
print("-------------------------------------")

'''If you want to create an array with the specific number you can use the following syntax: 
np.full(shape,value)'''
custom_Array = np.full((2,3),"y")
print(custom_Array)

print("-------------------------------------")

# numpy.arange() function creates an array of evenly spaced values within a given interval. It is similar to Python’s built-in range() function but returns a NumPy array instead of a list.
# numpy.arange(start, stop, step)
arr = np.arange(1,10,0.5)
print(arr)
print("-------------------------------------")

# Combining a conditional filtering :
filtered = arr[arr%2==0]
print(filtered)

print("-------------------------------------")
#creating an indentity matrix: 
iMatrix = np.eye(4)
print(iMatrix)


'''RANDOM ARRAYS'''
from numpy import random
r = random.randint(100,size = (4,4))# will create an random array of size 4
print(r)
r = random.rand(4,4)# will create an random array of size 4 with foat value
print(r)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
r = random.randint(100000, 900001, size=(4, 4))  # Random integers between 100000 and 900000
print(r)


# Create an array with random unique values :
RandomUniqueValueArray = random.choice(100,size = 10,replace=False)
print(RandomUniqueValueArray)
RandomUniqueValueArray = random.choice(np.arange(100,999),size = 10,replace=False)
print(RandomUniqueValueArray)

