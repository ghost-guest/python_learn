import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(data, index=labels)
# 31. 对 DataFrame 数据切片：
print(df2[1:3])
# 32. 对 DataFrame 通过标签查询（单列）：
print(df2['age'])
# 33. 对 DataFrame 通过标签查询（多列）：
print(df2[['age', 'animal']])
# 34. 对 DataFrame 通过位置查询：
print(df2.iloc[1:3])
# 35. DataFrame 副本拷贝：
df3 = df2.copy()
print(df3)
# 36. 判断 DataFrame 元素是否为空：
print(df2.isnull())
# 37. 添加列数据：
num = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], index=df3.index)
df3['NO.'] = num
print(df3)
# 38. 根据 DataFrame 的下标值进行更改。：
df3.iat[1, 1] = 2
print(df3)
# 39. 根据 DataFrame 的标签对数据进行修改
df3.loc['f', 'age'] = 15
print(df3)
# 40. DataFrame 求平均值操作：
print(df3.mean())
# 41. 对 DataFrame 中任意列做求和操作：
print(df3['age'].sum())