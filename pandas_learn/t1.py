import pandas as pd
import numpy as np

print(pd.__version__)


a = [1,2,3,4,5]
ser = pd.Series(a)
print(ser)

a = np.random.randint(1,10,5)
print(a)
index = ['a', 'b', 'c', 'e', 'f']
ser = pd.Series(a, index=index)
print(ser)

a = {'a': 1, "b": 2, 'c': 3}
ser = pd.Series(a)
print(ser)

