import pandas as pd
import numpy as np

# 修改series索引

a = np.random.randint(0,10,5)

ser = pd.Series(a)
print(ser)
ser.index = ['a', 'b', 'c', 'd', 'f']
print(ser)
# series 的纵向拼接
s2 = pd.Series({'a': 1, 'b': 2, "c": 3})
s3 = ser.append(s2)
print(s3)

# 8. Series 按指定索引删除元素：
s4 = s3.drop('a')
print(s4)
# 9. Series 修改指定索引元素：
s4['b'] = 'a'
print(s4)
# 10. Series 按指定索引查找元素：
print(s4['f'])
# 11. Series 切片操作：
print(s4[:3])
# 12. Series 加法运算：

print('+'*60)
print(ser)
print(s3)
s5 = s3.add(ser)
s6 = s3.sub(ser)
s7 = s3.mul(ser)
s8 = s3.div(ser)
print(s5)
print(s6)
print(s7)
print(s8)
print('=='*50)
# 16. Series 求中位数：
print(s3.median())
# 17. Series 求和：
print(s3.sum())
# 18. Series 求最大值：
print(s3.max())
# 19. Series 求最小值：
print(s3.min())
