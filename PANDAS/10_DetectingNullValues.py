'''
there are two type of missing values :
Nan : not a number;
None: for object datatype

use .isnull() for detecting the null value
if return ture : missing value present
if return false : missing vlaue not presetn
'''
import pandas as pd
data = {
    "name" : ["ram",None,"aryan","rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,None,21,34,54,32,None],
    "Salary": [129292,None,272734,848484,38222,585856,383737,272733],
}

df = pd.DataFrame(data)
print(df.isnull())# This will retrnn true if None is presetn
print(df.isnull().sum()) # this will returnt total number of the null values
print(df.isnull().sum()["age"]) # this will print the number of null values in the age column
