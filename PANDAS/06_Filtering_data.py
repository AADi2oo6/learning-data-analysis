#lets see how to filter the data 
import pandas as pd
# import numpy as np
from numpy import random
data = {
    "name" : ["ram","shayam","aryan","rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,33,21,34,54,32,53],
    "Salary": random.randint(10_000,90_000,size = 8 ),
    "PerformanceScore" :random.randint(80,100,size = 8)
}
df = pd.DataFrame(data)
print(df)

#selecting a single column
col = df["Salary"]
print(f"The data of the column is : \n {col}")

#selecting multiple column : 
Mcol = df[["Salary","age","PerformanceScore"]]
print(Mcol)

#filtering the data ; 
fsal = df[df["Salary"]>50000]
print(f"Salary greater then 50000 is given belwo : \n {fsal}")

MuliFilteredData = df[(df["Salary"]>40000) & (df["age"]<5)]
print(f"Salary > 40000 and age < 50 is\n{MuliFilteredData}")