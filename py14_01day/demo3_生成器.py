from collections.abc import Iterator, Iterable, Generator

"""
Iterable(可迭代对象)
    1、什么是可迭代对象？
        能够使用for循环进行迭代操作的都是可迭代对象
    2、python中内置的数据类型那些是可迭代对象？
        1、字符串，列表，元组，集合，字典，range对象，open打开的文件对象
        2、实现了序列语义的对象（对象拥有一个__getitem__方法）魔术方法
        3、实现了迭代协议的对象（对象拥有__iter__方法）
Iterator(迭代器)
    1、什么是迭代器？
        实现了迭代器协议的对象称为迭代器
    2、迭代器协议？构成迭代器协议的两个对象
        __iter__():返回迭代器对象本身
        __next__():从迭代器返回下一项
    3、迭代器特性？
        1、可以使用内置函数next进行逐个迭代取值
        2、当迭代器中的数据被迭代完之后，再去迭代会抛出一场：StopIteration
        3、迭代器中的数据只能被迭代一次
        
    注意：所有的可迭代对象都能够使用内置函数iter转换为 迭代器

Generator(生成器)
    1、生成器继承与迭代器，他是一个特殊的迭代器，拥有迭代器的所有特性
    2、生成器比迭代器多了3个方法：
        g.close()
        g.send()
        g.throw()
        
    3、如何定义生成器：
        1、生成器表达式：gener=(i for i in range(100))
            快速生成数据
        2、生成器函数：
            1、只要函数中有 yield 关键字，不管在什么位置，这个函数就叫生成器函数
            2、生成器调用时，不会执行内部的代码，会直接返回一个生成器对象
            
            3、关键字 yield 的作用？
                用来生成数据；
                yield关键字后边的内容就是生成出来的数据
                如果想通过函数生成器生成多个数据，需要将yield放在循环中使用
            
            4、怎么使用生成器生成数据？
                
    4、使用生成器有什么好处？
        在程序中存放百万级数据时，能够显著减少内存开下
        
    5、为什么生成器能够减少内存开销？
        生成器内部实际不存储数据，只保存数据生成的计算规则，几乎没有内存开销

"""

# 把可迭代对象转换为迭代器,iter()
li = [11,22,33,44]
li_iter = iter(li)
print("使用next：{}".format(next(li_iter)))
for i in li_iter:
    print(i)

# 通过列表推导式创建一个可迭代对象
list_iter = iter([i for i in range(100)])


def work():
    for i in range(10):
        print(f"---------{i}-----------")
        yield "python--{}".format(i)

# 通过next()方法进行遍历
g= work()
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))
# print("生成出来的数据是：", next(g))


# 通过for循环对生成器函数进行便利
for i in g:
    print("生成出来的数据是：", i)

# 使用list对生成器进行迭代，然后将所有的迭代出来的数据放到列表中
# res = list(g)
# print(res)