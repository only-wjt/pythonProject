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
# print(sorted(kictA.items(), key=lambda d: d[0]))
# 按照value进行排序
# print(sorted(kictA.items(), key=lambda d: d[1]))


print(kictA["str1"])
print('---------------------')
book = {}
book["书名"] = "天才在做，疯子在右"
book["价格"] = 30
book['作者'] = '高铭'
book['出版社'] = '人民出版社'
book.update({'价格': 30 * 0.8})
for key, value in book.items():
    print('%s==%s' % (key, value))

del book['书名']  # 删除一个字典
# v = book.pop("书名")  # 返回值
book.popitem()  # 删除最后一个并返回最后一个元组{key,value}
for key, value in book.items():
    print('%s==%s' % (key, value))

print('--------------------------')
books = [{'价格': 20, '名称': '流浪地球', '出版社': '人民出版社'}, {'价格': 20, '名称': '三体', '出版社': '人民出版社'}]
for book in books:
    del book['出版社']
    pass

print(books)

# 遍历和查询
print('=============================')
# books = [{'价格':20, '名称':'流浪地球','出版社':'人民出版社'},{'价格':20, '名称':'三体','出版社':'人民出版社'}]
book = {'价格': 20, '名称': '流浪地球', '出版社': '人民出版社'}
print(book.keys())
len(book)  # 返回几个键值对

book.get('价格')  # 对于去不存在的key，此种方法不会报错
print(book.get('价格1', '如果不存在，可以设置次默认值'))  # 相对于book['价格1']

for u in book:
    print(u)  # 取出的是key

for value in book.keys():
    print(book.get(value))

print(book.values())

print(book.items())  # [('价格', 20), ('名称', '流浪地球'), ('出版社', '人民出版社')]
for key, value in book.items():
    print("{}:{}".format(key, value))

print(book.fromkeys('价格', '555'))
print('--------------------------')
print('ssssekeu'.lower())
print('ssssekeu'.upper())

