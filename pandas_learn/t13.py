import pandas as pd
import numpy as np

# 74. 使用列表拼接多个 DataFrame：
temp_df1 = pd.DataFrame(np.random.randn(5, 4))  # 生成由随机数组成的 DataFrame 1
temp_df2 = pd.DataFrame(np.random.randn(5, 4))  # 生成由随机数组成的 DataFrame 2
temp_df3 = pd.DataFrame(np.random.randn(5, 4))  # 生成由随机数组成的 DataFrame 3

print(temp_df1)
print(temp_df2)
print(temp_df3)

pieces = [temp_df1, temp_df2, temp_df3]
a = pd.concat(pieces)
print(a)
# 75. 找出 DataFrame 表中和最小的列：
df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
print(df)
a = df.sum().idxmin()  # idxmax(), idxmin() 为 Series 函数返回最大最小值的索引值
print(a)
# 76. DataFrame 中每个元素减去每一行的平均值：
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
a = df.sub(df.mean(axis=1), axis=0)
print(a)
# 77. DataFrame 分组，并得到每一组中最大三个数之和：
df = pd.DataFrame({'A': list('aaabbcaabcccbbc'),
                   'B': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
print(df)
a = df.groupby('A')['B'].nlargest(3).sum(level=0)
print(a)
