# with the help of "info()" funciton we can find all the detail of the dataframe
'''
info()
    1. number of rows and columns
    2. columns names
    3. Data type info
    4. Nonn null values
    5. Memory usage of the dataframe
'''
import pandas as pd
df = pd.read_csv("sampleData.csv",encoding="latin1")
df_Small = pd.read_csv("BioData.csv")


print(f"Displaying the Info of the dataset : \n {df.info()}")
print(f"Disolaying the info of the Small data set : {df_Small.info()}")


'''Now lests see how can we get the number of rows and columns of the data
df.shape : returns the tupe (rows,columns)
df.columns : returns the columns names
'''
print(f"The number of rows and columns are : {df.shape}")
print(f"Columns names : {df.columns}")