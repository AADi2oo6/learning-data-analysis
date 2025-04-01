x = [100,200,300]
#Applying 10 perSent discoutn on a list
y = list(map(lambda p: 0.9*p , x))
print(y)

'''
BROADCASTING IS A NUMPY WAY TO PREFORM ARRAYS ON DIFFERENT SHAPE ARRAY WITHOUT USING LOOP
'''
import numpy as np
prices = np.array(x)
discount = 10

final_Price = (prices*0.9)
print(final_Price)