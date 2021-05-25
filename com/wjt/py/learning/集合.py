# 集合 set 关键字，无序的不重复的元素
# 作用 特点： 如果是数值，则会自动排序
import random

list1 = [1, 2, 4, 3, 5, 6, 6]

# 声明集合
s1 = set()  # 空集合只能用这种方式

s2 = {1, 'rr', 4, 3, 'dd'}

print(type(s1))
s3 = set(list1)
for i in list1:
    s1.add(i)  # 添加元素

print(s1)
print(s3)
print(s2)

t1 = ('林志玲', '言承旭')
s2.update(t1)  # 添加多个元素
s2.add(t1)  # 当成一个整体，放进集合中
print(s2)

# s2.remove()  # 移出不存在的元素则报错
# s2.pop()  # 删除第一个集合元素

s2.clear()  # 清空
# s2.discard()  # 移出不存在的元素，则不会报错

print('-------------------------------')
set1 = set()
for i in range(10):
    ran = random.randint(1,20)
    set1.add(ran)
print(set1)


print(6 in set1)
set5 = {1,2,3,5}
set6 = {1,2,3,5,6}
set7 = set6.difference(set5)  # 差集 相当于 -
print(set7)
set7 = set5.intersection(set6)  # &
print(set7)  # 交集

print('-------------------')
# 并集
set8 = set5 | set6
print(set8)

set8 = set5.union(set6)
print(set8)

l1 = [2,3,4,5,6,7]
l2 = [3,4,9,0,1]

# 对称差集 -->就是除了并集的，两个集合的其他所有元素
s1 = set(l1)
s2 = set(l2)
result = (s1 | s2) - (s1 & s2)
print(result)

result1 = s1 ^ s2  # s1.symmetric_difference()
print(result1)
