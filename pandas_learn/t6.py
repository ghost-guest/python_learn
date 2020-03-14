import pandas as pd
import numpy as np

# 42. 将字符串转化为小写字母：
string = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca',
                    np.nan, 'CABA', 'dog', 'cat'])
print(string)
a = string.str.lower()
print(a)

# 43. 将字符串转化为大写字母：
b = string.str.upper()
print(b)
# 44. 对缺失值进行填充：
a = string.copy()
print(a)
b = a.fillna(value=4)
print(b)
# 45. 删除存在缺失值的行：
a = string.copy()
print(a)
b = a.dropna(how='any')
print(b)
