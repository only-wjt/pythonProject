# 字符串
str1 = 'Hello world!!!'
str2 = "OnlyWjt"
print(str1+"::"+str2)

var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
print("--------------------------------")
print(var1[5:1:-1])
print("line1 \
... line2 \
... line3")

print("1111 \
2222 \
eeee")

print("退格符号：："+"hello \b world!!!")
print("\110\145\154\154\157\40\127\157\162\154\144\41")
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
print( r'\n' )
print('\n')


print("------------------------------")
print("我叫 %s 今年 %d岁" % ('王际涛', 26))


# 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
# 一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

print('----------------------------')
name = 'test'
print(f'{name} f-String')
print(f'{1*3+3}')
x = 1
print(f'{x+1=}')

str4 = 'This is the string associated with the test'
print('首字母大写自建函数'+str4.capitalize())

str5 = "[runoob]"
print("str.center(40, '*') : ", str5.center(40, '*'))

str = "[www.runoob.com]"
print ("str.center(4, '*') : ", str.center(4, '*'))

# enter()方法语法：str.center(width[, fillchar])
# fillchar 只能是单个字符  fillchar 默认是空格
# 奇数个字符时优先向右边补*
print('123'.center(4, '*'))
# 偶数个字符时优先向左边补*
print('1234'.center(5, '*'))

print('------------decode()方法语法：--------------')
# 语法：bytes.decode(encoding="utf-8", errors="strict")

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))


print('hello '.join('world'))
print(len('jjjjj'))

print('jjjjjjddddjd'.replace('j', 'k', 3))


if __name__ == '__main__':
    n = input("")
    s = "〇一二三四五六七八九"
    for c in "0123456789":
      n = n.replace(c, s[eval(c)])
    print(n)


