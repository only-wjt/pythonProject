# 元组是一种不可变的序列，在创建之后不能做任何修改 特点：不可变，2、()来创建，数据项用都好分割，3：可以是任何类型；4：当元组中只有一个元素时，要加上逗号，不然解释器会当成整形来处理 5、同样支持切片操作

tupleA = (1,)
print(type(tupleA))
tupleB = (1)
print(type(tupleB))  # 当元组中只有一个元素时，要加上逗号，不然解释器会当成整形来处理
tupleA = (1, 2, '4sss', 'rtrrrr', 7, 6, 9.283, [1, 2, 3])
print(tupleA)
# 元组的查询
for item in tupleA:
    print(item)

print(tupleA[2:4])
print(tupleA[1:4:-1])

tupleC = ();
print(id(tupleC))
tupleC = ('1', '2')
print(id(tupleC))

listA = []
print(id(listA))
listA = [1, 2]
print(id(listA))

# 如果元组中的其中一个元素是list，则可以进行修改
tupleD = (1, 2, [2, 3, 4])
print(tupleD)
print(type(tupleD[2]))
tupleD[2][1] = 8
print(tupleD)

tupleE = tuple(range(10))
print(tupleE.count(6))  # 在元组中存在几个8
