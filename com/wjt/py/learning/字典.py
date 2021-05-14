# 字典相当于java中的map，key不可变,通常试用key来获取数据
# 特点：1、不是序列类型，没有下表的概念。是一个无序的键值对集合，是python内置的数据类型
# 2、用{}来表示字典对象，每个用逗号分割
# 3、key必须是不可变类型，【字符串、元组】  值可以是任意类型
# 4、每个key是唯一的，存在相同key，后者会覆盖前者

kictA = {'str1': 'dddd', 'name': '王际涛', 'age': 18}
# 简单for循环
for int in range(20):
    kictA[str(int)] = int
print(kictA['str1'])
print(kictA)
arr = [];
print(len(kictA))
# 获取所有的key和值
print(kictA.keys())
print(kictA.values())
# 获取所有的键值对
print(kictA.items())
for key, value in kictA.items():
    print('%s==%s' % (key, value))

kictA.update({13: '222'})  # 如果存在，则执行更新，不存在，则新增
print(kictA)
print("------------------------删除---------------")
# del kictA[13]
# print(kictA)
# 排序
print(sorted(kictA.items(), key=lambda d: d[0]))
# 按照value进行排序
print(sorted(kictA.items(), key=lambda d: d[1]))
