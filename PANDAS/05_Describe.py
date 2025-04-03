

import pandas as pd
data = {
    "name" : ["ram","shayam","aryan",-"rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,33,21,34,54,32,53],
    "Salary": [21221,39393,494943,39393,234234,44555,123124,23412],
    "PerformanceScore" :[84,95,67,83,23,54,65,76]
}

df = pd.DataFrame(data)
print(df)

print(df.describe())

print(f"(rows,columns): {df.shape} \n columns names : {df.columns} \n size : {df.size}")

