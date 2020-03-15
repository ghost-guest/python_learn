import pandas as pd
import numpy as np

"""
数据清洗
常常我们得到的数据是不符合我们最终处理的数据要求，包括许多缺省值以及坏的数据，需要我们对数据进行清洗。

88. 缺失值拟合：

在FilghtNumber中有数值缺失，其中数值为按 10 增长，补充相应的缺省值使得数据完整，并让数据为 int 类型。
"""
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
print(df)
"""
89. 数据列拆分：

其中From_to应该为两独立的两列From和To，将From_to依照_拆分为独立两列建立为一个新表。
"""
temp = df.From_To.str.split('_', expand=True)
temp.columns = ['From', 'To']
print(temp)
"""
90. 字符标准化：

其中注意到地点的名字都不规范（如：londON应该为London）需要对数据进行标准化处理。
"""
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
print(temp)
"""
91. 删除坏数据加入整理好的数据：

将最开始的 From_to 列删除，加入整理好的 From 和 to 列。
"""
df = df.drop('From_To', axis=1)
df = df.join(temp)
print(df)
"""
92. 去除多余字符：

如同 airline 列中许多数据有许多其他字符，会对后期的数据分析有较大影响，需要对这类数据进行修正。
"""
df['Airline'] = df['Airline'].str.extract(
    '([a-zA-Z\s]+)', expand=False).str.strip()
print(df)

"""
93. 格式规范：

在 RecentDelays 中记录的方式为列表类型，由于其长度不一，这会为后期数据分析造成很大麻烦。
这里将 RecentDelays 的列表拆开，取出列表中的相同位置元素作为一列，若为空值即用 NaN 代替。
"""
delays = df['RecentDelays'].apply(pd.Series)

delays.columns = ['delay_{}'.format(n)
                  for n in range(1, len(delays.columns)+1)]

df = df.drop('RecentDelays', axis=1).join(delays)
print(df)


