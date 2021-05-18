sum = 0
for data in range(1, 101, 2):
    print(f'每个data值{data}')

# print("我叫 %s 今年 %d岁" % ('王际涛', 26))
# print(f'{name} f-String')
sum = 0
for item in range(1, 100):
    if item % 2 == 0:
        break
        print('不会执行')
        pass
    else:
        sum += 1
        print(f'zhixing{sum}此')
        pass

index = 1
while index <= 100:
    if index > 20:
        break
        pass
    index += 1
    print(index)

# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end=' ')
        pass
    print()
    pass

# for-----else
for item in range(1, 11):
    print(item, end=' ')
    if item > 5:
        break
    pass
else:  # 在上面的循环中，只要是出现了break,else中的代码就不会执行
    print("已经执行完了吗")  # 如果没找到，则可以提示

# 这块可以直接用for循环和if语句实现，但是这样写会更简洁
account = 'admin'
pwd = '123'
for i in range(3):
    zh = input("请输入账号：")
    mm = input("请输入密码：")
    if zh == account and mm ==pwd:
        print("登录成功")
        break
        pass
    pass
else:
    print("您的密码输入错误过多！")






