'''
Rehaping : changing the dimesions of the array without changing the content of the actual data
     SYNTAX: 
            reshape(rows,columns) 
        Note : reshape only works if dimesions match otherwise error
        Reshapeing array does not create a copy it returns a  <view>
'''
import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(3,2)
print("one dimensional array : \n",arr)
print("reshaped Array : \n",reshaped_arr)
print(arr)
print("----------------------------------------------")

'''Flatenning of the array : Convert multydimensional array to the 1d Array
.revel() -> views, means it affects the original array
.flatten() -> copy, means it don't affect the original array
Note : both method can be use to flatten the 2d array 
'''

array2D = np.array([[1,2,3],[4,5,6]])
print(f"This is the 2d array : \n {array2D}")
print(f"Printing using both the method : \n {array2D.flatten()} \n {array2D.ravel()}")
print(array2D)