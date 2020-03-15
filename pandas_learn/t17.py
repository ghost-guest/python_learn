import pandas as pd
import numpy as np

"""
数据预处理
94. 信息区间划分：

班级一部分同学的数学成绩表，如下图所示
"""
df=pd.DataFrame({'name':['Alice','Bob','Candy','Dany','Ella','Frank','Grace','Jenny'],'grades':[58,83,79,65,93,45,61,88]})
print(df)
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Candy', 'Dany', 'Ella',
                            'Frank', 'Grace', 'Jenny'],
                   'grades': [58, 83, 79, 65, 93, 45, 61, 88]})


def choice(x):
    if x > 60:
        return 1
    else:
        return 0


df.grades = pd.Series(map(lambda x: choice(x), df.grades))
print(df)
"""
95. 数据去重：

一个列为A的 DataFrame 数据，如下图所示
"""
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
print(df)
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
a = df.loc[df['A'].shift() != df['A']]
print(a)
"""
96. 数据归一化：

有时候，DataFrame 中不同列之间的数据差距太大，需要对其进行归一化处理。	
"""
def normalization(df):
    numerator = df.sub(df.min())
    denominator = (df.max()).sub(df.min())
    Y = numerator.div(denominator)
    return Y


df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
a = normalization(df)
print(a)
