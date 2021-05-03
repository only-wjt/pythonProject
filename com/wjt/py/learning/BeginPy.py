import keyword

# 输出所有关键字
print(keyword.kwlist)
'''
这是第一行代码
'''
print("hello world")

if False:
    print("TRUE")
else:
    print("FLASE")

total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

print(total)
word = '字符串'
i = 1
str = """这是一
ddd
个字符串"""
str1 = '''ddd


dddd'''

print(i)
print(str)
print(str1)

str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

import sys;

x = 'runoob';
sys.stdout.write('\n' + x)

y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
# print(x, end=" ")
# print(y, end=" ")
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(d)

t = [1, 2, 3, 4, 5]
print(t[0])
print(t[1:3])
print(t[1:-1])
print(t[1:])

print('---------')

t = [1, 2, 3, 4, 5, 6]
print(t[1:5:3])
print(t[1:4])

print('--------')
s = 'abcdefgh'
print(s[5:1:-1])
print(s[::-2])
print(s[5:0])

print('--------')
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 为空，因为1在-6左边，但是step为-1,两边矛盾，所以取不出来值
print(arr[1:-6:-1])
# 注意：如果start_index和end_index决定的取值方向和step决定的方向不一样，则取不到值
print(arr[-1:6:-1])
# 多层切片操作，相当于一个数组多次切片
arr[:8][2:5][-1:]
# 切片操作的三个参数可以用表达式
arr[2 + 1:3 * 2:7 % 3]

print("-------拷贝-------")
b = arr[::]
print(b)
print(id(arr))
print(id(b))

print("-------")
print(arr[::-1])
'''
总结
 参考 https://www.jianshu.com/p/15715d6f4dad
（一）start_index、end_index、step三者可同为正、同为负，或正负混合。但必须遵循一个原则，即：当start_index表示的实际位置在end_index的左边时，从左往右取值，此时step必须是正数（同样表示从左往右）；当start_index表示的实际位置在end_index的右边时，表示从右往左取值，此时step必须是负数（同样表示从右往左），即两者的取值顺序必须相同。
（二）当start_index或end_index省略时，取值的起始索引和终止索引由step的正负来决定，这种情况不会有取值方向矛盾（即不会返回空列表[]），但正和负取到的结果顺序是相反的，因为一个向左一个向右。
（三）step的正负是必须要考虑的，尤其是当step省略时。比如a[-1:]，很容易就误认为是从“终点”开始一直取到“起点”，即a[-1:]= [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]，但实际上a[-1:]=[9]（注意不是9），原因在于step省略时step=1表示从左往右取值，而起始索引start_index=-1本身就是对象的最右边元素了，再往右已经没数据了，因此结果只含有9一个元素。
（四）需要注意：“取单个元素（不带“:”）”时，返回的是对象的某个元素，其类型由元素本身的类型决定，而与母对象无关，如上面的a[0]=0、a[-4]=6，元素0和6都是“数值型”，而母对象a却是“list”型；“取连续切片（带“:”）”时，返回结果的类型与母对象相同，哪怕切取的连续切片只包含一个元素，如上面的a[-1:]=[9]，返回的是一个只包含元素“9”的list，而非数值型“9”。
step：正负数均可，其绝对值大小决定了切取数据时的‘‘步长”，而正负号决定了“切取方向”，正表示“从左往右”取值，负表示“从右往左”取值。当step省略时，默认为1，即从左往右以步长1取值。“切取方向非常重要！”“切取方向非常重要！”“切取方向非常重要！”，重要的事情说三遍！
start_index：表示起始索引（包含该索引对应值）；该参数省略时，表示从对象“端点”开始取值，至于是从“起点”还是从“终点”开始，则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。
end_index：表示终止索引（不包含该索引对应值）；该参数省略时，表示一直取到数据“端点”，至于是到“起点”还是到“终点”，同样由step参数的正负决定，step为正时直到“终点”，为负时直到“起点”。
'''

'''
python中浅拷贝只是拷贝最外层的元素，如果其中一个元素是一个对象的地址，则改变这个对象的元素，远数组也会变化，深拷贝，是拷贝的整个内容
'''

print("--------------字典---------")
# 字典
dic = {"name1": "wanghuibin", "name2": "guxia", "name3": "wangjitao"}
print(dic['name1'])
print(dic.keys())
print(dic.values())

dict = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dict)
dict1 = {x: x**2 for x in (2, 4, 6)}
print(dict1)

print('---------------')
sss = 'ssssssss'
print(tuple(sss))
