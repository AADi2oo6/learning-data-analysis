#aggregation function : what it does
'''
np.sum(array): returns the sum fo all the elements of the array
np.mean(array): will retrunt he mean of the array
min(array): returns the minimum value of the array;
max(array): returns the max value of the array;
np.std(array) returns the standerd deviation of the array;
np.var(array) returns the varience of the array:
'''
import numpy as np 
arr = np.array([10,20,30,40,50])
print(max(arr))
print(min(arr))
print(arr.mean())
print(arr.sum())
print(arr.std())
print(arr.var())