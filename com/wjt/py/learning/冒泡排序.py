# 冒泡排序
arr = [23, 12, 45, 33, 56, 43]
arr.sort()
print(arr)

# 方式1
# num = int(input('请输入一个数字'))
# for i in range(len(arr)):
#     if(arr[i] <= num and (arr[i+1]) > num):
#         arr.insert(i+1,num)
#         pass
#         break
#         pass
#     pass
# print(arr)

# 方式2
# number = int(input("请输入一个数字"))
# for i in arr:
#     if number <= i:
#         arr.insert(arr.index(i), number)
#         break
#         pass
#     pass
# else:
#     arr.append(number)
# print(arr)

# 交换
a = 2;
b = 3;
c = 8;
a, b = b, a
print(a, b)
a, b, c = b, a, c
print(a, b, c)

# 手写冒泡排序
arr = [23, 12, 45, 33, 56, 43]
print(range(0, len(arr) - 1))
for j in range(0, len(arr) - 1):
    for i in range(0, len(arr) - 1 - j):
        if arr[i] > arr[i + 1]:
            arr[i+1],arr[i] = arr[i],a[i+1]
            # a = arr[i]
            # arr[i] = arr[i + 1]
            # arr[i + 1] = a
            pass
        pass
    pass
print(arr)
