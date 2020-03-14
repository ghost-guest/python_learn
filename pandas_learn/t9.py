import pandas as pd
import numpy as np

# 51. 建立一个以 2018 年每一天为索引，值为随机数的 Series：
dti = pd.date_range(start='2018-01-01', end='2018-12-31', freq='D')
s = pd.Series(np.random.rand(len(dti)), index=dti)
print(s)
# 52. 统计s 中每一个周三对应值的和：
# 周一从 0 开始
a = s[s.index.weekday == 2].sum()
print(a)
# 53. 统计s中每个月值的平均值：
b = s.resample('M').mean()
print(b)

