# ndarray.shape retuns the tuple conating the size of the array
# ndarray.ndim return the dimension of the array
# ndarray.size returns the total number of the elements of the array
# ndaray.dtype returns the data type of the array

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", arr.shape)  
print("Dimensions:", arr.ndim)  
print("Size:", arr.size) 
print("Data type:", arr.dtype)  
print("Item size:", arr.itemsize)  
