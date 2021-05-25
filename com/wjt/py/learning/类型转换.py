# str() int() list() dict() set() tuple()
# str -->int,list.set.tuple  反过来也可以
s = '80'
i = int(s)
print(type(i))

s = 'abc'
i = list(s)
print(type(i))

s = set(s)
print(type(s))

t = tuple(s)
print(type(t))

# list --> set(), tuple(),dict()[转成字典需要这种格式[(key,value),(key.value)]]
tuple = (1, 2, 3, 4)
print(list(tuple))
set = {1, 2, 3, 4}
print(list(set))

dict = {1: 2, 3: 4}
print(list(dict))  # 只是将key放入list中
