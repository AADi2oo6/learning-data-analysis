import numpy as np


#1D array
arr1 = np.array([1, 2, 3, 4, 5])

#2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

#3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr1)
print(arr2)
print(arr3)


a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])
print(a)
print(b) 
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(a*b)


# numpy.arange() function creates an array of evenly spaced values within a given interval. It is similar to Python’s built-in range() function but returns a NumPy array instead of a list.
# numpy.arange(start, stop, step)
arr = np.arange(1,10,0.5)
print(arr)

# Combining a conditional filtering :
filtered = arr[arr%2==0]
print(filtered)