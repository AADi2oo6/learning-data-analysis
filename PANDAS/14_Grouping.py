# how to group the data of a datafram
'''syntax: 
df.groupby("columnNmae")["DAtaofColumnYouWant"].sum()
NOTE: summ is an aggrigation function 
.sum() : returns the sum 
.count(): return the count of non Nan values
.mean(): return the mean of the data
.min(): return the minimum value
.max(): reutnr the max value
.std(): return the standerd deviation
'''
import pandas as pd
data = {
    "name" : ["ram","amit","aryan","rohan","Avinash","Aditya","Soham","Veda"],
    "age" : [21,31,30,33,21,31,21,30],
    "Salary": [129292,121333,272734,848484,38222,585856,383737,272733],
}
df = pd.DataFrame(data)

print("---------------------------------------")
group = df.groupby("age")#This will create a group on the basis of the age
for i in group: #group of every column will be formed withe the unique values of age
    print(i[0],'\n',i[1])



print("---------------------------------------")
groupSalary = df.groupby("age")["Salary"] # this will create group of unique age withe all the Salaries of that age
for i in groupSalary:
    print(i[0],'\n',i[1])


print("---------------------------------------")
grouped = df.groupby("age")["Salary"].sum()#this will print the age and sum of the salary of that age
print(grouped)

print("---------------------------------------")
'''GROUP BY MULTIPLE DATA'''
gData = df.groupby(["age","name"])["Salary"].sum()
print(gData)