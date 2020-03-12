import pandas as pd
import numpy as np

# 20. 通过 NumPy 数组创建 DataFrame：
dates = pd.date_range('today', periods=6)  # 定义时间序列作为index
num = np.random.randn(6, 4)  # 随机数作为列表内容
print(num)
columns = ['A', 'B', 'C', 'D']  # 列表的列名
df = pd.DataFrame(num, index=dates, columns=columns)
print(df)
