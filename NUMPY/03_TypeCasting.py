# Change the data types of the array using astype() function
'''Syntax: 
array.astype(int)
'''
import numpy as np

arr= np.array([23.3,5.3,45.2,56.34])
int_arr = arr.astype(int)
print(arr.dtype,"---->",int_arr.dtype)
print(arr,"---->",int_arr )