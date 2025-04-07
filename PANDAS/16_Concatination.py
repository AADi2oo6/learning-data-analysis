# Concatination is the process of mergin 2 data frame along row or axis
'''
vertically : row-wise
horizontly : column wise

pd.concate([df1,df2],axis = 0, ignore_index = True)
                        0 for row wise
                        1 for column wise
'''
import pandas as pd
data1 = {
    "id" : [1,2,3],
    "name":["Aditya","Aryan","Rohan"]
}
data2 = {
    "id" : [5,4,6],
    "name": ["Sohame","harsh","vedant"]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df_contat = pd.concat([df1,df2],axis=0,ignore_index=True)
print(df_contat.sort_values("id"))
df_contat = pd.concat([df1,df2],axis=1,ignore_index=True)
print(df_contat)