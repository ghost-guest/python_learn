import pandas as pd
import numpy as np

# 21. 通过字典数组创建 DataFrame：
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(data, index=labels)
print(df2)
# 22. 查看 DataFrame 的数据类型：
print(df2.dtypes)
# 23. 预览 DataFrame 的前 5 行数据：
print(df2.head())
# 24. 查看 DataFrame 的后 3 行数据：
print(df2.tail(3))
# 25.查看 DataFrame 的索引：
print(df2.index)
# 26. 查看 DataFrame 的列名：
print(df2.columns)
# 27. 查看 DataFrame 的数值：
print(df2.values)
# 28. 查看 DataFrame 的统计数据：
print(df2.describe())
# 29. DataFrame 转置操作：
print(df2.T)
# 30. 对 DataFrame 进行按列排序：
a = df2.sort_values(by='age')
print(a)