#boolean masking : filtering data based on condition:
import numpy as np 
arr = np.array([1,22,3,4,45,890342,65,7534,123])
filterd_Array = arr[arr>100]
print(filterd_Array)