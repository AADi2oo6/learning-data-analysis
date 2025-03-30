import numpy as np

arr = np.array([10,20,30,40,50])
print(arr[3]) # will print the item at the index 3
print(arr[1:4]) # will print the items from index 1 to 4

print("Mylti-Dimensional Array : Slicing")
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)

#NOTE : indexing starts from 0
print("for printing element of column  index x and row index y : arr2[x,y]")
print(arr2[1,2]," : represent elements at row index1 and column index2")
print(arr2[2,2], " : represnt elements at row index2 and column index2")

# CREATING A SUB-MATRIX
print("Creating a sub-matrix")
print(arr2[1:3,1:3])# represent the sub-matrix from row index 1 to 3 and column index 1 to 3 

# Sub-matrix from rows 0-1, columns 1-2
print(arr2[0:2, 1:3])  