import pandas as pd
import numpy as np

# 54. 将 Series 中的时间进行转换（秒转分钟）：
s = pd.date_range('today', periods=100, freq='S')

ts = pd.Series(np.random.randint(0, 500, len(s)), index=s)

a = ts.resample('Min').sum()
print(a)
# 55. UTC 世界时间标准：
s = pd.date_range('today', periods=1, freq='D')  # 获取当前时间
ts = pd.Series(np.random.randn(len(s)), s)  # 随机数值
ts_utc = ts.tz_localize('UTC')  # 转换为 UTC 时间
print(ts_utc)
# 56. 转换为上海所在时区：
b = ts_utc.tz_convert('Asia/Shanghai')
print(b)
# 57.不同时间表示方式的转换：
rng = pd.date_range('1/1/2018', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
ps = ts.to_period()
print(ps)
c = ps.to_timestamp()
print(c)
