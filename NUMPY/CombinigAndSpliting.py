# Joining tow array in python is not as semiple as a list : 
# we have to use the Concatenate() function to join tow or more arrays
import numpy as np

arr1 = np.array([2,4,6])
arr2 = np.array([1,4,5])

print(f"the conbination of array1 and array2 is : {np.concatenate([arr1,arr2])}") 

# IN case of multi-dimensional array we have to specify the axis along which wwe want to join the arrays
arr1 = np.array([[10,20],[30,40]])
arr2 = np.array([[5,6],[7,8]])
print(f'adding array1 and array2 along axis 0 (row wise): \n{np.concatenate([arr1,arr2],axis = 0)}')# off you can use np.vstack([arr1,arr2])
print(f"using vstack to stack the element row wise:\n {np.vstack([arr1,arr2])}")
print(f"Adding array1 and array2 along axis 1 (column wise): \n{np.concatenate([arr1,arr2],axis = 1)}")# orr you can use pn.hstack([arr1,arr2])
print(f"using hstack to stack the element column wies : \n {np.hstack([arr1,arr2])}")


# spliting an array : 
# syntax :  np.array_split(<arrayName>,<numberOfarray>)
a = np.array([12,34,67,564,8228,987])
print(f"Splited array is given by : \n {np.array_split(a,2)}")
b,c = np.array_split(a,2)
print(b,c)

# for tow dimensional arrays split creats an aray of differeent row
arr3  = np.array([b,c])
print(f'the 2d array is given by : \n{arr3}')
print(f'splited arrays are: \n{np.array_split(arr3,2)}')