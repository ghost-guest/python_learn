import pandas as pd
import numpy as np

# 47. CSV 文件写入：
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(data, index=labels)
print(df2)
df2.to_csv('animal.csv')
print("写入成功.")
# 48. CSV 文件读取：
df_animal = pd.read_csv('animal.csv')
print(df_animal)
# 49. Excel 写入操作：
df2.to_excel('animal.xlsx', sheet_name='Sheet1')
print("写入成功.")
# 50. Excel 读取操作：
a = pd.read_excel('animal.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(a)
