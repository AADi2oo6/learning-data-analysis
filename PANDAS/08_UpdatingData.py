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

#  we can use the .lco() function to updata the data of a dataset
# df.loc[index,"columnName"] = new data

df.loc[7,"age"] = 19 # this way we can update value of single element of column
print(df)

# Method to update the whole column of the dataset is given below
# Now if i want to add .emp to the end of the name of the every employee:
df["name"] +=".emp"
print(df)

for i in range(len(df["age"])):
    if df["age"][i]>40:
        df.loc[i,"age"] = df["age"][i]-20
print(df)
