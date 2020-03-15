import pandas as pd
import numpy as np

"""
绝对类型
在数据的形式上主要包括数量型和性质型，数量型表示着数据可数范围可变，
而性质型表示范围已经确定不可改变，绝对型数据就是性质型数据的一种。

83. 绝对型数据定义
"""
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": [
                  'a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")
print(df)
# 84. 对绝对型数据重命名：

df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df)
# 85. 重新排列绝对型数据并补充相应的缺省值：
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"])
print(df)
# 86. 对绝对型数据进行排序：
a = df.sort_values(by="grade")
print(a)
# 87. 对绝对型数据进行分组：
a = df.groupby("grade").size()
print(a)
