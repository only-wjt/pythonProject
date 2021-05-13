# list：python中非常重要的数据结构，是一种有序的数据集合
# 特点：1、支持增删改查，2、数据项发生改变,3、数据可以是任意类型，4、支持索引和切片进行操作

li = [1, 2, 3, 4, '你好']
print(type(li))
print(len(li))
print(len('ssssddd'))

listA = ['abcd', 785, 13.23, '求职', True]
# print(listA[1:2:-1])
# print(listA[1:3])
# print(listA[3:1:-1])
# print(listA[::-1])
# print(listA * 3)  # 输出多次列表中数据
print('--------------------------增加元素-------------------------')
print(listA)
listA.append(['ffff', 'ddd'])
listA.append('888')
print('追加之后', listA)
listA.insert(1, '44 ')
print('插入之后的数据', listA)
raData = list(range(10))
print(type(raData), raData)
listA.extend(raData)  # 扩展，等于批量添加
print(listA)
print('-------------------------修改元素-----------------')
listA = ['abcd', 785, 13.23, '求职', True]
listA[0] = 'peter'
print(listA)
del (listA[0])
del listA[1:2]
print(listA)
listA.pop(0)
print(listA)
listB = range(10, 20)
print(listB)
print(listB.index(12))  # 返回索引小标







