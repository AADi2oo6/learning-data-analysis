# we can remove the column of a the data frame using the drop function

import pandas as pd
from numpy import random 
import numpy as np
data = {
    "name" : ["ram","shayam","aryan","rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,33,21,34,54,32,53],
    "Salary": random.randint(10_000,90_000,size = 8 ),
    "PerformanceScore" :random.randint(80,100,size = 8)
}

df = pd.DataFrame(data)
print(df)

df.drop(columns=["PerformanceScore"], inplace = True) #inplace = trure meanse make change in the original datafrom 
print(df)