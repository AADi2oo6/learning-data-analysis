#how to create a csv file using pandas
import pandas as pd

data = {
    "Name" : ["Aditya","Aryan","Soham"],
    "Age" : [19,19,20],
    "City": ["Aurangabad","Nagpur","Nashik"]
}
df = pd.DataFrame(data) #This will convert this data to a dataframe
print(df)
df.to_csv("BioData.csv",index=False)#index = false means not to write index number in the data
 
#how to conver to excel file 
df.to_excel("BData.xlsx", index = False)
df.to_json("BData.json", index = False)
