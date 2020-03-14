import pandas as pd
import numpy as np

# 46. DataFrame 按指定列对齐：
left = pd.DataFrame({'key': ['foo1', 'foo2'], 'one': [1, 2]})
right = pd.DataFrame({'key': ['foo2', 'foo3'], 'two': [4, 5]})

print(left)
print(right)

# 按照 key 列对齐连接，只存在 foo2 相同，所以最后变成一行
a = pd.merge(left, right, on='key')
print(a)

