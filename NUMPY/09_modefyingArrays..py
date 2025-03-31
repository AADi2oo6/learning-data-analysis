# methods to modefy the arrays (add, remove, stack or split)
'''arrays in python have fixed size so for preforming any modification we have to crete a new array : 
'''


import numpy as np
arr=np.array([1,2,3,4,5])
print(f'The origina array is : {arr}')


#Inserting an element to the array: Syntax -> np.insert(array,index,value,axes = none )
#for 2d array  axes = 0  means inserting data RowWise and 1 mens column wise
arr1 = np.insert(arr,5,666)
print(f"used the insert fucnction and added 6 at index 5 : {arr1}")

#INSERTING IN 2D ARRAY: 
arr2d = np.array([[1,2,3],[4,5,6]])
#         insert(array,index, value,  axis)
arr2 = np.insert(arr2d,   1  ,[33,66],axis = 1)
print(f'using insert in 2d array : \n {arr2}')

#NOTE: if axis is equal to none it will flaten the array and insert the value
arr2 = np.insert(arr2d, 1, [33,66],axis  = None)
print(f"Array if axis is equal to zero : \n {arr2}")