import pandas as pd
from numpy import random
data = pd.read_excel("BData.xlsx")
df = pd.DataFrame(data)
print(df)
df.insert(0,"Id",random.choice([23,42,54,23,23],size = 3))
print(df)
df.to_excel("BData.xlsx", index = False)