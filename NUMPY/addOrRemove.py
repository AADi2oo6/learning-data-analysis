# How to add or remove items from a array: 
# np.append(array,value) appends itmes to an array
# np.delete(array,index) removes items from an array
# np.insert(array,index,valuee) inserts an element to a array

import numpy as np
arr = np.arange(1,5)
print(arr)#[1 2 3 4]
arr1 =np.append(arr,np.arange(6,11))
print(arr1)#[ 1  2  3  4  6  7  8  9 10]

arr2 = np.array([[10,20],[30,40]])# in case of multy-dimesionla data pass axis to get the matrx
# all the input arrays must have same number of dimensions
print(np.append(arr2,[[5,6],[7,8]],axis = 1))
print(np.append(arr2,[[5,6],[7,8]],axis = 0))

#INSERTING VALUS IN A ARRAY
print(np.insert(arr1,4,5))#[ 1  2  3  4  5  6  7  8  9 10]
print(f"insering value in 2d array: \n {arr2}")
print(np.insert(arr2,1,[1,2],axis = 1))
# 
print(np.insert(arr2,(0,1),[999],axis = 0))


#DELETING AN ELEMENT FROM A ARRAY
print(f"deleting elemsnts form a array: \n{arr2}")
print(f"deleting 1ts index row(axis = 0 ) of a arry : \n{np.delete(arr2,1,axis = 0)}")
print(f'deleting 1st index column(axis = 1) of a array: \n{np.delete(arr2,1,axis=1)}')
