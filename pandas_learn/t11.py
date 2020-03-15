import pandas as pd
import numpy as np

# 58. 创建多重索引 Series：
letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])  # 设置多重索引
s = pd.Series(np.random.rand(30), index=mi)  # 随机数
print(s)
# 59. 多重索引 Series 查询：
# 查询索引为 1，3，6 的值
a = s.loc[:, [1, 3, 6]]
print(a)
# 60. 多重索引 Series 切片：
b = s.loc[pd.IndexSlice[:'B', 5:]]
print(b)
print("="*90)
# 61. 根据多重索引创建 DataFrame：
frame = pd.DataFrame(np.arange(12).reshape(6, 2),
                     index=[list('AAABBB'), list('123123')],
                     columns=['hello', 'shiyanlou'])
print(frame)
# 62. 多重索引设置列名称：
frame.index.names = ['first', 'second']
print(frame)
# 63. DataFrame 多重索引分组求和：
c = frame.groupby('first').sum()
print(c)
# 64. DataFrame 行列名称转换：
print(frame)
d = frame.stack()
print(d)
# 65. DataFrame 索引转换：
print(frame)
f = frame.unstack()
print(f)
