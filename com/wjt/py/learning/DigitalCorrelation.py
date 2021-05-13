import math
from math import ceil
from random import shuffle

nubmer1 = 1
print(nubmer1)
del nubmer1

number2 = [1, 2, 3]
number3 = [4, 5, number2]
del number3[number2[1]];
print(number2)
print(number3)
# 注意：在不同的机器上浮点运算的结果可能会不一样。
# 在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
print(17 / 3)
print(17 // 3)
print(17 % 3)
print(5 * 3 + 2)
# 注意：//得到的不一定是整数类型，它与分母分子的数据类型有关系
print(7 // 2)
print(7.0 // 2)
print(7 // 2.0)
print(2 << 3)  # 位移运算

print("----------------数学函数---------------")
print(abs(-10))
print(ceil(4.1))  # 向上取整
listArr = [1, 2, 3]
print("--------------------------------------")
math.pi
print(math.pi)
print(math.log(100, 10))
print(max(1, 2, 3))
print(math.modf(100.22))
print(math.pow(1, 2))
round(102.322, 2)
print(math.sqrt(4))
