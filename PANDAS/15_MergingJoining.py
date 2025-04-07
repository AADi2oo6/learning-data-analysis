# df.merge(df1,df2,on = "Common_column",how = "merge Type")
import pandas as pd 

data1 = {
    "Id": [1,2,3,4],
    "Name": ["Aryan","Avinash","Rohan","Soham"]
}
data2 = {
    "Id" : [1,2,5,4],
    "Salary":[20000,30000,24000,45000]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# inner join : if common column data present in both the df then only show the data

innerJoin = pd.merge(df1,df2,on = "Id",how = "inner")
print(f"INNER JOin \n{innerJoin}")

# outer join : merges data on common column but if common data not present reuturn nan
# outer join contains all the data of both the df
outerJoin = pd.merge(df1,df2,on= "Id",how = "outer")
print(f"Outer Join \n{outerJoin}")

# left join : will keep only data of left df column which matchs with right df column If right does't have data of left return nan
leftjoin = pd.merge(df1,df2, on = "Id",how = "left")
print(f"Left Join \n{leftjoin  }")

# right join : will keep data of right and try to match it with left df
rightJoin = pd.merge(df1,df2,on = "Id",how ="right")
print(f"RightJoin \n{rightJoin}")


'''THE LAST ONE IS THE CROSS JOIN
df1 = n rows and df2 = m rows 
then corss join will have m*n rows

'''