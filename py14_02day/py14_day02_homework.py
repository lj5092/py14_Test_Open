#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 9:52 下午
# @Author  : LiangJun
# @Filename    : py14_day02_homework.py

from faker import Faker
"""
1、现在有一个列表   li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22],
请将 大于5的数据过滤出来，然后除以2取余数，结果放到一个生成器中

2、定义一个可以使用send传入域名，自动生成一个在前面加上http://，在后面加上路径/user/login的url地址，

生成器最多可以生成5个url,生成5条数据之后再去生成，则报错StopIteration

使用案例：

# 例如:
res = g.send('www.baidu.com')
# 生成数据res为：http://www.baidu.com/user/logim'

3、面试笔试扩展题
有一个正整数列表(数据是无序的,并且允许有相等的整数存在),
编写一个能实现下列功能的函数，传入列表array,和正整数X，返回下面要求的2个数据
def func(array, x)
    '''逻辑代码'''
    return count, li
1、统计并返回在列表中,比正整数x大的数有几个(相同的数只计算一次)，并返回-----返回值中的的count
2、计算列表中比正整数X小的所有偶数，并返回  -----------返回值中的li
"""

# 1、请将 大于5的数据过滤出来，然后除以2取余数，结果放到一个生成器中
li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22]
li1 = [i % 2 for i in li if i > 5]
li_g = (i for i in li1)
print("第一题打印出来的结果", end=": ")
for i in li_g:
    print(i, end=' ')

print()


# 2、定义一个可以使用send传入域名，自动生成一个在前面加上http://，在后面加上路径/user/login的url地址,
# 生成器最多可以生成5个url,生成5条数据之后再去生成，则报错StopIteration
def http():
    add = yield
    for i in range(5):
       add = yield "http://{}/user/login".format(add)
add_http = http()
print("第二题打印出的结果：")
next(add_http)
print(add_http.send('www.baidu.com'))
print(add_http.send('www.sina.com'))
print(add_http.send('www.souhu.com'))
print(add_http.send('www.yongyou.com'))
print(add_http.send('www.haha.com'))
# print(add_http.send('www.cuowu.com'))


# 3、1、统计并返回在列表中,比正整数x大的数有几个(相同的数只计算一次)，并返回-----返回值中的的count
# 2、计算列表中比正整数X小的所有偶数，并返回  -----------返回值中的li


list_one = [i for i in range(30)]
list_tow = [11,22,11,22,22,11,8,8]


def func(array, x):
    # 第一种去重：
    # list_null = []
    # list1 = [list_null.append(i) for i in array if i not in list_null]

    # 第二种去重
    list_null = list(set(array))
    print(list_null)
    count = 0
    li = []
    for i in list_null:
        if i > x:
            count += 1
        elif i < x and i%2==0:
            li.append(i)
    return count, li

print("第三题：")
a, b = func(list_tow, 10)
print("比正整数大的一共有：{} 个".format(a))
print("比正整数小的偶数有：{}".format(b))

fake = Faker(locale='zh_CN')
print(fake.name())

def work():
    number = yield
    while True:
        if number == 1:
            number = yield fake.name()
        elif number == 2:
            number = yield fake.phone_number()
        elif number == 3:
            number = yield fake.address()
        else:
            number = yield {'name:':fake.name(), 'phone_number:':fake.phone_number(), 'add':fake.address()}

g = work()
next(g)
print('生成的内容：', g.send(4))
print('生成的内容：', g.send(1))
print('生成的内容：', g.send(2))
print('生成的内容：', g.send(3))

