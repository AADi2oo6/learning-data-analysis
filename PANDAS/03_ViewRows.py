#Methods to view the rows of the data with the help of "head() and tail() methods"
'''
head(n) : will display the first n rows of the dataset if n not given return first 5 rows
tail(n) : similarly displays last n rows if n not passed returns the last 5 rows
'''

import pandas as pd

df = pd.read_csv("sampleData.csv",encoding="latin1")
print(f"first 10 rows of the data \n {df.head(10)}")
print(f"last 10 rows of the data \n {df.tail(10)}")
