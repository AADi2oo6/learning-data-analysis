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

# creating a new column using assingment opperator; syntax => df["column name"] = [data]
df["bonus"] = 1.1*df["Salary"]
print(df)

# Using the insert function we can add a column at any position(Mostly used);
'''
df.insert(loc,"columnName",data)
'''
d = random.choicef(np.arange(100,999),size = 8, replace=False)
df.insert(0,"ID",d)
print(df)