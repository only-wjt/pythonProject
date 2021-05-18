# 这是onlyWjt的首个方法
def reverseWords(input):
    # 通过空格将字符串分割，吧各个单词各位列表
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords[::-1]
    outPut = ' '.join(inputWords)
    return outPut


if __name__ == '__main__':
    input = 'shanghai like i'
    rw = reverseWords(input)
    print(rw)


# lis、元组、字典的共有操作
# + --> 同类型的类型才能使用此符号，不同类型会报错
strA = '人生苦短'
strB = '我用python'
print('sss'+strA+strB+'sss')
listA = [1, 2]
listB = [3, 4]
print(listA+listB)

print('人' in strA)
print(1 in listA)

dict = {'name': '吴彦祖'}
# 只能判断key
print('age' in dict)

