import numpy as np
from numpy import random
r  = random.choice(16,size = (4,4))
print(r)

index  = np.where(r == 0)
print(index[0])