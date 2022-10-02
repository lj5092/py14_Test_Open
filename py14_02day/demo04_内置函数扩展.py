#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 8:56 下午
# @Author  : LiangJun
# @Filename    : demo04_内置函数扩展.py
"""
1、filter，过滤器
2、map
"""

#1、 filter 过滤器:filter的返回值是一个迭代器
# 参数1：过滤规则函数
# 参数2：过滤对象
li = [13,24,56,1,64,23,78,16,90]
res = filter(lambda x: x> 30, li)
print(list(res))

# 2、map，批量的做数据处理(线程池和进程池需要用到map处理)
# 参数1：处理数据的函数
# 参数2：可迭代对象
li1 = ["{'a':11,'b':22}",'[33,44,55]']
res1 = map(lambda x: eval(x), li1)
print(list(res1))

# 需求：通过input输入一组数据，使用空格隔开，生成一个列表
# arr = input("请输入一组数据，并使用空格隔开：")
# res2 = list(map(int, arr.split(' ')))
# print(res2)

# 3、exec 执行字符串里边的python代码
s = "a = 12\nb = 13\nprint(a+b)"
exec(s)
# 也可以执行文件中的pyton内容
code = open('code.txt', 'r', encoding='utf-8').read()
exec(code)

# 4、all，迭代函数内所有的元素为真
name = '张三'
age = 18
sex = 'xl'
if all([name, age, sex]):
    print("成立")

# 5、any，迭代函数内有一个元素为真，返回Ture
if any([name, age, sex]):
    print("成立")

# 6、zip，聚合打包,zip(列表1，列表2)：以列表1当键，列表2当值组成字典
case = [['case_id', 'title', 'url', 'data', 'execpted'],
        ['1', '用例1', 'www.baidu.com', '001', 'ok'],
        ['2', '用例2', 'www.souhu.com', '002', 'ok']]

abc = []
for i in range(len(case)):
    if i > 0:
        abc.append(dict(zip(case[0], case[i])))
print(abc)


new_case = [dict(zip(case[0], case[i])) for i in range(len(case)) if i > 0]
print(new_case)