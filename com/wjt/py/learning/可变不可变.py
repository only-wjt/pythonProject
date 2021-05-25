# 不可变：对象所致想的内存中的值是不可变的 int str float tuple


s1 = 'abd'
print(id(s1))
s1 = 'abdc'
print(id(s1))

tuple = (1, 2, 3)
print(id(tuple))
tuple = (1, 2)
print(id(tuple))

# 可变:该对象所指向内存中的值是可以改变的  list dict set
print('--------------可变---------------')
list1 = [1, 2, 3, 4]
print(list1, id(list))
list1.pop()
print(list1, id(list))

dict = {1: 'aa', 2: 'cc'}
print(id(dict))
dict.pop(1)
print(id(dict))

set = {1, 2, 3}
print(id(set))
set.pop()
print(id(set))
