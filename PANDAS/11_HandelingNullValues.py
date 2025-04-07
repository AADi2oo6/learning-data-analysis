# thear are verious ways to handel the null values 1 is by deleting the null values
'''
.dropna(axes = 0or1 , inplace =true) will delete the 0(row with null value)
                1(columns with the null values) inplace = true for makeing changes in the original dataframe
                default axis = 0;
'''
import pandas as pd
data = {
    "name" : ["ram","amit","aryan","rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,47,21,34,54,32,None],
    "Salary": [129292,None,272734,848484,38222,585856,383737,272733],
}

df = pd.DataFrame(data)
# df.dropna(axis = 0,inplace = True) # or df.dorpna(inplace = ture) are same will delete rows with null values
print(df)
df.dropna(axis=1,inplace=True)
print(df)

'''Lets see how to replace the null value with other values'''
#.fillna(value,inplace = true) : With the help of this function we can fill the empty places
df = pd.DataFrame(data)
print(df)

# df.fillna(0,inplace = True)#handeling the null vaues default values;
# print(df)

# filling the null values with calculated value
# df["age"].fillna(abs(df["age"].mean()),inplace = True)
df.fillna({"age":df["age"].mean()},inplace = True)# thi is the new syntax


print(df)