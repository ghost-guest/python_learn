import pandas as pd
import numpy as np

"""
当分析庞大的数据时，为了更好的发掘数据特征之间的关系，且不破坏原数据，就可以利用透视表 pivot_table 进行操作。

78. 透视表的创建：

新建表将 A, B, C 列作为索引进行聚合。
"""
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})

print(df)

a = pd.pivot_table(df, index=['A', 'B'])
print(a)
"""
79. 透视表按指定行进行聚合：

将该 DataFrame 的 D 列聚合，按照 A,B 列为索引进行聚合，聚合的方式为默认求均值。
"""
a = pd.pivot_table(df, values=['D'], index=['A', 'B'])
print(a)
"""
80. 透视表聚合方式定义：

上一题中 D 列聚合时，采用默认求均值的方法，若想使用更多的方式可以在 aggfunc 中实现。
"""
a = pd.pivot_table(df, values=['D'], index=['A', 'B'], aggfunc=[np.sum, len])
print(a)
"""
81. 透视表利用额外列进行辅助分割：

D 列按照 A,B 列进行聚合时，若关心 C 列对 D 列的影响，可以加入 columns 值进行分析。
"""
a = pd.pivot_table(df, values=['D'], index=['A', 'B'],
               columns=['C'], aggfunc=np.sum)
print(a)
"""
82. 透视表的缺省值处理：

在透视表中由于不同的聚合方式，相应缺少的组合将为缺省值，可以加入 fill_value 对缺省值处理。
"""
a = pd.pivot_table(df, values=['D'], index=['A', 'B'],
               columns=['C'], aggfunc=np.sum, fill_value=0)
print(a)
