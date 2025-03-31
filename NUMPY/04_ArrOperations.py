import numpy as np
arr = np.array([1,2,4,5])
print(arr**3) 
print("-------------------------------")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(f"array1 : {arr1} \narray2 : {arr2}")
print("-------------------------------")
# ELEMENT WISE OPERATIONS ON ARRAYS
print(f"Sum of array1 and array2 is : {arr1+arr2}")
print("-------------------------------")
print(f"Diff of array1 and array2 is : {arr1-arr2}")
print("-------------------------------")
print(f"Product of array1 and array2 is : {arr1*arr2}")
print("-------------------------------")
print(f"Div of array1 and array2 is : {arr1/arr2}")
print("-------------------------------")

# MATRIX OPPERATIONS ON ARRAYS:

matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])
print("matrix1 and matrix2 are provided bewlow: ")
print("-------------------------------")
print(f"{matrix1}\n{matrix2}")
print("-------------------------------")

print(f"value of matrix1 with power of 3 is : \n{np.power(matrix1,3)}")
print("-------------------------------")
print(f"the Square root of matrix2 is : \n {np.sqrt(matrix2)}")
print("-------------------------------")
print(f"dot product of matrix1 and matrix2 is : \n {np.dot(matrix1,matrix2)}")
print("-------------------------------")

