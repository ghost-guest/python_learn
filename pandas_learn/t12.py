import pandas as pd
import numpy as np

# 66. DataFrame 条件查找：
# 示例数据
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
print(df)
# 查找 age 大于 3 的全部信息
a = df[df['age'] > 3]
print(a)
# 67. 根据行列索引切片：
b = df.iloc[2:4, 1:3]
print(b)
# 68. DataFrame 多重条件查询：
# 查找 age<3 且为 cat 的全部数据。

df = pd.DataFrame(data, index=labels)

a = df[(df['animal'] == 'cat') & (df['age'] < 3)]
print(a)
# 69. DataFrame 按关键字查询：
a = df[df['animal'].isin(['cat', 'dog'])]
print(a)
# 70. DataFrame 按标签及列名查询。：
a = df.loc[df.index[[3, 4, 8]], ['animal', 'age']]
print(a)
# 71. DataFrame 多条件排序：
#
# 按照 age 降序，visits 升序排列
a = df.sort_values(by=['age', 'visits'], ascending=[False, True])
print(a)
# 72.DataFrame 多值替换：
# 将 priority 列的 yes 值替换为 True，no 值替换为 False。
a = df['priority'].map({'yes': True, 'no': False})
print(a)
# 73. DataFrame 分组求和：
a = df.groupby('animal').sum()
print(a)
