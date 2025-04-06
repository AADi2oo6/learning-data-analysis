#boolean masking : filtering data based on condition:
import numpy as np 
from numpy import random
arr = np.array([1,22,3,4,45,890342,65,7534,123])
filterd_Array = arr[arr>100]
print(filterd_Array)

'''how to locate an element of an array using ".where()" '''

arr = np.array([4, 7, 2, 7, 9, 7, 6])

# Find the first occurrence of 7
index = np.where(arr == 7)[0][0]  # Get the first index

print("Index of first occurrence of 7:", index)


# Create an array with random unique values :
RandomUniqueValueArray = random.choice(100,size = 10,replace=False)
print(RandomUniqueValueArray)
RandomUniqueValueArray = random.choice(np.arange(100,999),size = 10,replace=False)
print(RandomUniqueValueArray)

