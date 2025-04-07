# lets insert data on the baseis of interpretation
import pandas as pd
data = {
    "name" : ["ram","amit","aryan","rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,30,None,21,34,26,35],
    "Salary": [129292,121333,272734,848484,38222,585856,383737,272733],
}
df = pd.DataFrame(data)
# lets predict the None value of the age using interloation
df.interpolate(method="linear",axis=0,inplace=True)
# there are various method avilable eg: linear, polynomial, time etc

print(df)


data1 = {
    "slot" : [1,2,3,4,5,6],
    "coins": [10,20,None,40,None,60]
}
df1 = pd.DataFrame(data1)
# lets use interpolation in single column only
print(df1)

df1["coins"] = df1["coins"].interpolate(method = "linear")
print(df1)