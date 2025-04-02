#Handeling Missing values in Numpy : 
'''BUILT IN FUNCTIONS : 
np.innan() -> detects missing vaslues  (RETURNS THE BOOLEAN VALUE)
np.nan_to_num() -> replace missing values to number (default number will be zero)
np.isinf() ->for detecting infinite numbers
nan -> stand for "NOT A NUMBER"
'''
#NOTE: nan values can't be compared

import numpy as np
arr = np.array([1,2,3,np.nan,4,np.nan,23,])
print(np.isnan(arr))
#FOR Replacing this number using nan_to_num function 

# cleaned_arr = np.nan_to_num(arr) hear default replacing number is 0
cleaned_arr = np.nan_to_num(arr,nan = -1)
print(cleaned_arr)

arr = np.array([123,2342,5324,np.inf,523,-np.inf])
print(np.isinf(arr))

#NOTE: how to replace the inf numbers
'''using the nan_to_num(arr,posinf=1,neginf = 2) we have to set the value of 
+ve infinity and -ve infinity saperately
'''
cleand_arr = np.nan_to_num(arr,posinf=1000,neginf=-100)
print(cleand_arr)