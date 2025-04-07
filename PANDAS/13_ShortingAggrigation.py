# Shorting and aggrigation in pandas
'''for shorting data of a column use : sort_values() function
df.sort_values(by= "column name", assanding = True/false,inplace = true)
'''

import pandas as pd
data = {
    "name" : ["ram","amit","aryan","rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,30,32,21,34,26,35],
    "Salary": [129292,121333,272734,848484,38222,585856,383737,272733],
}
df = pd.DataFrame(data)
df1 = df.sort_values(by= "name",ascending = True,inplace=False)
print(df1)

# lets apply shorting in multiple columns
df2= df.sort_values(by=["age","Salary"],ascending=[True,False],inplace = False)
print(df2)                                   #     age , salary