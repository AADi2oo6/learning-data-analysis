#STAKING AND SPLITTING OF THE ARRAY: there are two way to stack the array (horizontly or VerticallY)
'''
=======STACKING=========
vstack() -> for vertical stacking
hstack() -> for horizontal stacking
'''
import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

V_Stacked_Array = np.vstack((arr1,arr2))
H_Stacked_Array = np.hstack((arr1,arr2))

print(f"Vertically stacked array : \n {V_Stacked_Array} \n Horizontally stacked array : \n {H_Stacked_Array}")



'''
========SPLITTING===========
split() : for dividing in equal parts

hsplit() : for horizontal Splitting
vsplit() : for vertical splitting
'''

arr = np.array([1,2,3,4,5,6])
print(np.split(arr,3)) # throws error if equal parts can't be created

arr2 = np.array(np.split(arr,2))
print(f"given array : \n {arr2}")
print(f'Vsplit array \n {np.vsplit(arr2,2)}')
print(f'hsplit array \n {np.hsplit(arr2,6 )}')
