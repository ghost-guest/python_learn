'''
@Author: ghost-guest
@Date: 2020-02-22 13:45:27
@LastEditTime: 2020-02-22 14:09:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit 
@FilePath: /pyenv/pandas1/test1.py
'''
import numpy as np
import pandas1 as pd
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv(
    'https://labfile.oss.aliyuncs.com/courses/1283/telecom_churn.csv')
# 查看表格前5行的数据
title_head = df.head()
print(title_head)
# 查看数据的维度
shape = df.shape
print("="*30)
print(shape)
# 获取列名
col = df.columns
print(col)
#print dataframe's general information
info = df.info()
print("-"*40)
print(info)
df['Churn'] = df['Churn'].astype('int64')
print("==="*40)
print(df.describe(include=['object','bool']))
print("---"*30)
print(df['Churn'].value_counts(normalize=True))
print(df.sort_values(by='Total day charge', ascending=False).head())
print("++"*40)
print(df.sort_values(by=['Churn', 'Total day charge'],ascending=[True, False]).head())

print("----"*50)
print(df['Churn'].mean())




